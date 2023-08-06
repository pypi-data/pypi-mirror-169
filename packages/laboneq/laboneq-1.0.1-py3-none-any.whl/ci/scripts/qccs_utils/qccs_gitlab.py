import os
import gitlab


SERVER_URL = os.environ["CI_SERVER_URL"]
PRIVATE_TOKEN = os.environ["LOCAL_QCCS_API_WRITE_ACCESS_TOKEN"]
PROJECT_ID = os.environ["CI_PROJECT_ID"]
COMMIT_SHA = os.environ["CI_COMMIT_SHA"]

gl = gitlab.Gitlab(SERVER_URL, private_token=PRIVATE_TOKEN)
project = gl.projects.get(PROJECT_ID)


def get_mr():
    if "CI_MERGE_REQUEST_IID" in os.environ:
        mr_iid = os.environ["CI_MERGE_REQUEST_IID"]
    else:
        commit = project.commits.get(COMMIT_SHA)
        related_mrs = commit.merge_requests()
        if len(related_mrs)==0:
            print(f"No MR found related to commit {COMMIT_SHA}.")
            return None
        if len(related_mrs)>=1:
            mr_iid = related_mrs[0]["iid"]
            if len(related_mrs)>1:
                print(f"More than one MR found related to commit {COMMIT_SHA}. Will update note on MR {mr_iid}.")
    mr = project.mergerequests.get(mr_iid)
    return mr


def add_mr_comment(message, mr):
    if mr is not None:
        prefix = message.partition('\n')[0]
        for note in mr.notes.list():
            if note.body.startswith(prefix):
                # If note's and message's first line match:
                note.delete()

        # Add new note with the message
        mr.notes.create({'body': message})
        print("Note updated:")
        print(message)
        