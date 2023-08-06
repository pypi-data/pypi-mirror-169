import gitlab
import datetime
import re
import click


PATTERN_NIGHTLY = re.compile(r".*nightly.*")
NOW = datetime.datetime.now()


@click.command()
@click.option(
    "--gitlab-server",
    required=True,
    help="The URL of the gitlab server."
)
@click.option(
    "--project-id",
    required=True,
    help="The project id in gitlab."
)
@click.option(
    "--token",
    required=True,
    help="The API authentication token."
)
@click.option(
    "--threshold-nightly",
    default=180,
    type=int,
    help="The number of days to keep packages from nightly builds.",
    show_default=True
)
@click.option(
    "--threshold-default",
    default=30,
    type=int,
    help="The default number of days to keep packages (e.g. not from nightly builds).",
    show_default=True
)
@click.option(
    "--dry-run",
    is_flag=True,
    default=False,
    help="Dry run: no package will be deleted, log keep/delete for each package instead.",
    show_default=True
)
def main(
    gitlab_server,
    project_id,
    token,
    threshold_nightly,
    threshold_default,
    dry_run
):
    delta_default = datetime.timedelta(days=threshold_default)
    delta_nightly = datetime.timedelta(days=threshold_nightly)
    gl = gitlab.Gitlab(gitlab_server, private_token=token)
    project = gl.projects.get(project_id)
    packages = project.packages.list(all=True)

    if dry_run:
        print("Dry run. Actual execution would perform the following actions:")

    for package in packages:
        delta = delta_nightly if PATTERN_NIGHTLY.match(package.version) else delta_default
        creation_date = datetime.datetime.strptime(package.created_at.split("T")[0], '%Y-%m-%d')
        if dry_run:
            if NOW - delta > creation_date:
                print(f"Delete package {package.name}, version {package.version}, created {creation_date}.")
            else:
                print(f"Keep package {package.name}, version {package.version}, created {creation_date}.")
        else:
            if NOW - delta > creation_date:
                package.delete()
                
    
if __name__ == "__main__":
    main()