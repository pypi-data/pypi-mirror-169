import os

file_cwd = os.path.dirname(os.path.realpath(__file__))


class neuromancer:
    name = "neuromancer"
    setup_controller_handle = "neuromancer"
    wiring = os.path.join(file_cwd, "neuromancer.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "8004"
    power_switch = "powerswitch41.zhinst.com"


class neuromancer_shfqa:
    name = "neuromancer_shfqa"
    setup_controller_handle = "neuromancer_shfqa"
    wiring = os.path.join(file_cwd, "neuromancer_shfqa.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "8004"
    power_switch = "powerswitch41.zhinst.com"


class wintermute:
    name = "wintermute"
    setup_controller_handle = "wintermute"
    wiring = os.path.join(file_cwd, "wintermute.yml")
    server_host = "zidevel-09.zhinst.com"
    server_port = "8004"
    power_switch = "powerswitch20.zhinst.com"


class wintermute_shfqa:
    name = "wintermute_shfqa"
    setup_controller_handle = "wintermute_shfqa"
    wiring = os.path.join(file_cwd, "wintermute_shfqa.yml")
    server_host = "zidevel-09.zhinst.com"
    server_port = "8004"
    power_switch = "powerswitch20.zhinst.com"

class seacucumber_gen1:
    name = "seacucumber_gen1"
    setup_controller_handle = "seacucumber_gen1"
    wiring = os.path.join(file_cwd, "seacucumber_gen1.yml")
    server_host = "127.0.0.1"  # dummy server, until one is defined for SeaCucumber
    server_port = "8004"
    power_switch = "powerswitch25.zhinst.com"

class seacucumber_gen2:
    name = "seacucumber_gen2"
    setup_controller_handle = "seacucumber_gen2"
    wiring = os.path.join(file_cwd, "seacucumber_gen2.yml")
    server_host = "127.0.0.1" # dummy server, until one is defined for SeaCucumber
    server_port = "8004"
    power_switch = "powerswitch25.zhinst.com"


class countzero:
    name = "countzero"
    setup_controller_handle = "countzero"
    wiring = os.path.join(file_cwd, "countzero.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "8014"
    power_switch = "powerswitch21.zhinst.com"

class countzero_gen2:
    name = "countzero_gen2"
    setup_controller_handle = "countzero_gen2"
    wiring = os.path.join(file_cwd, "countzero_gen2.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "8014"
    power_switch = "powerswitch21.zhinst.com"

class flatline:
    name = "flatline"
    setup_controller_handle = "flatline"
    wiring = os.path.join(file_cwd, "flatline.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "8024"
    power_switch = "powerswitch51.zhinst.com"

class flatline_shfqc:
    name = "flatline_shfqc"
    setup_controller_handle = "flatline_shfqc"
    wiring = os.path.join(file_cwd, "flatline_shfqc.yml")
    server_host = "zidevel-04.zhinst.com"
    server_port = "18004"
    power_switch = "powerswitch51.zhinst.com"

class dry_run:
    name = "dry_run"
    wiring = os.path.join(file_cwd, "countzero.yml")
    server_host = ""
    server_port = "0"
