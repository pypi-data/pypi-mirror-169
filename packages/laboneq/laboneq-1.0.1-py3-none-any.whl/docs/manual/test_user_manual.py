import pytest
import subprocess
from pathlib import Path
import os.path
import shutil
import typing as t

ALLOWED_ERRORS = ["error - iconv: ISO8859-1 -> UTF-8"]
ALLOWED_WORDS = ["Grünberg", "Jülich"]


def hunspell_spelling() -> t.List[str]:
    """Run hunspell on all html files in user manual

    Returns:
        List of errors and spelling mistakes
    """
    hunspell_call = "find . -iname '*.html' -type f -exec \
        hunspell -l -i UTF-8 -d spelling_dict/en_US,spelling_dict/en_zhinst -H {} \;"
    p = subprocess.run(
        hunspell_call,
        cwd=os.path.dirname(os.path.realpath(__file__)),
        shell=True,
        capture_output=True,
    )
    errors = [
        x for x in p.stderr.decode("utf-8").split("\n")[:-1] if x not in ALLOWED_ERRORS
    ]
    if errors:
        return errors

    misspellings = set(
        [x for x in p.stdout.decode("utf-8").split("\n")[:-1] if x not in ALLOWED_WORDS]
    )
    return misspellings


def test_spelling():
    errors = hunspell_spelling()
    if errors:
        pytest.fail("\n".join(errors), False)


def html_check() -> str:
    """Run htmltest on all html files in user manual

    https://github.com/wjdp/htmltest

    Returns:
        log output of the htmltest call
    """
    pwd = Path(os.path.dirname(os.path.realpath(__file__)))
    yaml_config_text = f"""\
        DirectoryPath: {pwd}/build/qccs_sw_user_manual
        OutputDir: test_result
        IgnoreURLs:
            - "https://docs.zhinst.com/index.html"
            - "www.zhinst.com/downloads"
            - "http://<instrument-serial>.<domain>/"
            - "http://<instrument-serial>.local/"
            - "http://<instrument-serial>/"
            - "http://192.168.11.2/"
            - "http://192.168.1.10/"
            - "http://localhost.*"
        IgnoreInternalURLs:
            - "../release_notes.html"
        LogLevel: 3
        ExternalTimeout: 60
        IgnoreSSLVerify: true"""

    yaml_config_path = pwd / "test_result/html_test.yml"
    yaml_config_path.parents[0].mkdir(parents=True, exist_ok=True)
    with yaml_config_path.open("w", encoding="utf8") as yaml_config:
        yaml_config.write(yaml_config_text)

    subprocess.run(
        f"htmltest --conf {pwd}/test_result/html_test.yml", cwd=pwd, shell=True
    )

    log_file = pwd / "test_result/htmltest.log"
    fail_message = ""
    with open(log_file, "r") as log_message:
        fail_message = log_message.read()
    shutil.rmtree(log_file.parents[0])

    return fail_message


def test_html():
    fail_message = html_check()
    if fail_message != "":
        pytest.fail(fail_message, False)
