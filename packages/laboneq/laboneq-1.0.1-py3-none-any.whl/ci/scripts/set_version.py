import os
import subprocess
from datetime import datetime


COMMIT_HASH = os.environ["CI_COMMIT_SHORT_SHA"]
MASTER_VERSION_FILE_NAME = os.environ["MASTER_VERSION_FILE_NAME"]
VERSION_FILE_PATH = os.environ["VERSION_FILE_PATH"]
GITLAB_USER_NAME = os.environ["GITLAB_USER_NAME"]
GITLAB_USER_EMAIL = os.environ["GITLAB_USER_EMAIL"]
REMOTE_TEST_RELEASE = os.environ["TEST_QCCS_INTERNAL_REPO_URL"]
LOCAL_QCCS_REPO_URL = os.environ["LOCAL_QCCS_REPO_URL"]
RELEASE_PHASE = os.environ["RELEASE_PHASE"]


def main():
    # Validate version type
    if RELEASE_PHASE not in ["alpha", "beta", "release", "nightly"]:
        raise Exception(f"Unsupported version type: {RELEASE_PHASE}")
    # Read version from MASTER_VERSION_FILE_NAME
    with open(MASTER_VERSION_FILE_NAME, "r") as f:
        master_version = f.read().split("VERSION=")[1].strip()
    # Set laboneq/VERSION.txt
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if RELEASE_PHASE == "alpha":
        version = f"{master_version}a{date}+{COMMIT_HASH}"
    if RELEASE_PHASE == "nightly":
        version = f"{master_version}a{date}+nightly.{COMMIT_HASH}"
    if RELEASE_PHASE == "beta":
        version = f"{master_version}b{date}+{COMMIT_HASH}"
    if RELEASE_PHASE == "release":
        version = master_version
    with open(VERSION_FILE_PATH, "w") as f:
        print(f"Version: {version}", flush=True)
        f.write(version)
    # Add repo tag for release
    if RELEASE_PHASE in ["beta", "release"]:
        remote_name = "origin"
        remote_url = LOCAL_QCCS_REPO_URL
        if RELEASE_PHASE == "beta":
            remote_name = "test_release"
            remote_url = REMOTE_TEST_RELEASE
        try:
            subprocess.run(
                ["git", "remote", "set-url", remote_name, remote_url],
                check=True,
            )
        except:
            subprocess.run(
                ["git", "remote", "add", remote_name, remote_url],
                check=True,
            )
        print(
            f"Set {version} as tag on git commit {COMMIT_HASH} as user {GITLAB_USER_NAME} ({GITLAB_USER_EMAIL}) in remote {remote_name}.",
            flush=True,
        )
        subprocess.run(
            ["git", "config", "user.name", GITLAB_USER_NAME],
            check=True,
        )
        subprocess.run(
            ["git", "config", "user.email", GITLAB_USER_EMAIL],
            check=True,
        )
        subprocess.run(
            ["git", "tag", "-a", version, "-m", f"Release {version}", COMMIT_HASH],
            check=True,
        )
        subprocess.run(
            ["git", "push", remote_name, version],
            check=True,
        )


if __name__ == "__main__":
    main()
