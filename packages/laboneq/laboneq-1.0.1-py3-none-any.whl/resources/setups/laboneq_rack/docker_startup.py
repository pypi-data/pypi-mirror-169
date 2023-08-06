#!/usr/bin/env python3

import docker
import getpass
import argparse
import time

client = docker.from_env()
username = getpass.getuser()
container_name = username + '_servers'

# default server ports
webserver_port = 8006
dataserver_port = 8004
labone_version_str = '21.02'


try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', default=webserver_port, type=str, help="The name of the server container")
    parser.add_argument('--wsport', default=webserver_port, type=int, help="The port forwarding for webserver")
    parser.add_argument('--dsport', default=dataserver_port, type=int, help="The port forwarding for dataserver")
    parser.add_argument('--labver', default=labone_version_str, type=str, help="The Labone version you want to use")
    parser.add_argument('--device', type=str, help="Device to pass through")
    args = parser.parse_args()

except argparse.ArgumentError as err:
    print('ArgumentError: ' + str(err))
    print('Exiting')
    exit(1)

if args.name is not None:
    container_name = args.name

if args.device is not None:  # replicate read-write device path inside container
    args.device = args.device + ':' + args.device + ':rwm'
    print('Device passthrough not implemented')
    exit(1)

try:
    client.networks.list('labnet')[0]
except:
    print('Network labnet not found')
    print('Please create network using e.g.:')
    print('docker network create -d macvlan --subnet=192.168.1.0/24 --ip-range=192.168.1.24/24  -o parent=ens33 labnet')
    exit(1)

user_containers = client.containers.list(filters={'name': container_name})
for container in user_containers:
    print('stopping existing container ' + container_name)
    container.stop(timeout=1)

if user_containers:
    time.sleep(1)

labone_registry_entry = 'docker-registry.zhinst.com/devops/dockerfiles/labone_lin:' + args.labver
container_ports = {str(8006) : args.wsport, str(8004) : args.dsport}

try:
    print('starting new container ' + container_name)
    environment_vars = {'LABONE_DS_ARGS' : '--open-override 1 --auto-connect 0'}
    client.containers.run(labone_registry_entry, name=container_name, environment=environment_vars,
            privileged=True,  # ToDo: pass through specific devices instead of giving the VM full serial access
                              #       ... seems to be buggy specifically with this docker API package
            user='root',  # ToDo: add USB-access udev rules for the 'ci' user instead of running as root
            ports=container_ports, remove=True, detach=True)
    client.networks.list('labnet')[0].connect(container_name)

except docker.errors.APIError as err:
    print('ApiError: ' + str(err))
    print('Exiting')
    exit(1)

print(container_name + ' status is ' + client.containers.get(container_name).status)

