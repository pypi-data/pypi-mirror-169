import os
import glob
from wheel_inspect import inspect_wheel
from qccs_utils import qccs_gitlab


RELEASE_PHASE = os.environ["RELEASE_PHASE"].title()
PACKAGE_REGISTRY_URL = os.environ["LOCAL_QCCS_PACKAGE_REGISTRY_URL"]
DEPLOY_USER_NAME = os.environ["LOCAL_QCCS_BETA_TESTER_USER_NAME"]
DEPLOY_TOKEN = os.environ["LOCAL_QCCS_BETA_TESTER_DEPLOY_TOKEN"]


def format_message():
    title_prefix = "#" if RELEASE_PHASE=="Release" else f"# {RELEASE_PHASE}"
    wheel_files = glob.glob("build/laboneq/*.whl")
    index = PACKAGE_REGISTRY_URL.find("gitlab")
    index_url = f"{PACKAGE_REGISTRY_URL[:index]}{DEPLOY_USER_NAME}:{DEPLOY_TOKEN}@{PACKAGE_REGISTRY_URL[index:]}/simple"

    message = (
        f"{title_prefix} Release Notes: Python Package\n"
        "## Published versions\n"
    )
    for filename in wheel_files:
        wheel_info = inspect_wheel(filename)
        wheel_name = wheel_info["dist_info"]["metadata"]["name"]
        wheel_version = wheel_info["dist_info"]["metadata"]["version"]
        message += f"{wheel_name}: `{wheel_version}`\n"
    message += (
        "## Installation\n"
        "```\n"
    )
    for filename in wheel_files:
        message += f"pip3 install --upgrade {wheel_name}=={wheel_version} --extra-index-url \"{index_url}\"\n"
    message += "```"
    return message


def main():
    mr = qccs_gitlab.get_mr()
    message = format_message()
    qccs_gitlab.add_mr_comment(message, mr)


if __name__ == "__main__":
    main()
