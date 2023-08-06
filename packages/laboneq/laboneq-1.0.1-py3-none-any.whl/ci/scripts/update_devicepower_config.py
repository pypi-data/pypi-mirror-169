import inspect

import requests
import yaml

from resources.setups.laboneq_rack.laboneq.rack import setups


DEVICEPOWER_URL = "http://qccs-devicepower.zhinst.com/configuration_force"


def load_setups():
    setups_data = {}
    setup_list = [
        obj
        for name, obj in inspect.getmembers(setups)
        if inspect.isclass(obj) and name != "dry_run"
    ]
    for setup in setup_list:
        setups_data[setup.name] = {}
        setups_data[setup.name]["powerswitch"] = setup.power_switch
        setups_data[setup.name]["handle"] = setup.setup_controller_handle
        with open(setup.wiring, "r") as file:
            setups_data[setup.name]["wiring"] = yaml.full_load(file.read())
    return setups_data


def format_request_payload(setups_data):
    payload = {"powerswitches": {}}
    devices = {}
    for setup in setups_data:
        power_switch_tag = setups_data[setup]["powerswitch"].split(".")[0]
        if not power_switch_tag in payload["powerswitches"]:
            payload["powerswitches"][power_switch_tag] = {}
        for instrument_type in setups_data[setup]["wiring"]["instrument_list"]:
            for instrument in setups_data[setup]["wiring"]["instrument_list"][
                instrument_type
            ]:
                outlet = f"outlet{instrument['power_socket']}"
                device = f"{instrument_type}-{instrument['address']}"
                print(f"processing {outlet}/{device}")
                # Check that we are not overwriting an outlet
                if outlet in payload["powerswitches"][power_switch_tag]:
                    current_device = payload["powerswitches"][power_switch_tag][outlet][
                        "dev"
                    ]
                    if current_device != device:
                        raise Exception(
                            f"Trying to overwrite device in {power_switch_tag} {outlet}: {current_device}->{device}."
                        )
                # Check if device already assigned to another outlet
                if device in devices and devices[device] != outlet:
                    raise Exception(
                        f"Trying to re-assign {device} to {power_switch_tag} {outlet}. Already assigned to {devices[device]}."
                    )
                # If the current device is already assigned to the current outlet
                if outlet in payload["powerswitches"][power_switch_tag]:
                    # But the current label is not yet in the outlet's label list
                    labels = payload["powerswitches"][power_switch_tag][outlet]["label"]
                    if setups_data[setup]["handle"] not in labels:
                        # Add the label to the outlet's label list
                        payload["powerswitches"][power_switch_tag][outlet][
                            "label"
                        ] = ",".join([labels, setups_data[setup]["handle"]])
                # General case, assign a new device to a new outlet
                else:
                    payload["powerswitches"][power_switch_tag][outlet] = {
                        "label": setups_data[setup]["handle"],
                        "dev": device,
                    }
                devices[device] = outlet
    return f"---\n\nversion: '1.0'\n\n{yaml.dump(payload)}"


def main():
    setups_data = load_setups()
    request_data = format_request_payload(setups_data)
    try:
        requests.post(DEVICEPOWER_URL, data=request_data)
    except ConnectionError:
        pass


if __name__ == "__main__":
    main()
