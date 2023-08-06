import os
from qccs_utils import qccs_gitlab


REGISTRY = os.environ["CI_REGISTRY"]
IMAGE_NAME = os.environ["IMAGE_NAME"]
RELEASE_PHASE = os.environ["RELEASE_PHASE"].title()


def format_message():
    title_prefix = "#" if RELEASE_PHASE=="Release" else f"# {RELEASE_PHASE}"

    with open("../../laboneq/VERSION.txt", "r") as version:
        image_tag = version.read().replace("+", "-").strip()

    message = (
        f"{title_prefix} Release Notes: Test Bench\n"
        "## Tag Name\n"
        f"`{IMAGE_NAME}:{image_tag}`\n\n"
        "## Running Examples\n\n"
        "```\n"
        "# login to container registry if required\n"
        f"docker login {REGISTRY}\n\n"
        "# run the docker image interactively (shell prompt)\n"
        f"docker run -it {IMAGE_NAME}:{image_tag}\n"
        "or use the nightly build\n"
        f"docker run -it {IMAGE_NAME}:nightly\n\n"
        "# run the docker image interactively and with port binding (as required for Jupyter Notebooks)\n"
        f"docker run -it -p 8888:8888 {IMAGE_NAME}:{image_tag}\n"
        "or use the nightly build\n"
        f"docker run -it -p 8888:8888 {IMAGE_NAME}:nightly\n"
        "```"
    )
    return message


def main():
    mr = qccs_gitlab.get_mr()
    message = format_message()
    qccs_gitlab.add_mr_comment(message, mr)


if __name__ == "__main__":
    main()
