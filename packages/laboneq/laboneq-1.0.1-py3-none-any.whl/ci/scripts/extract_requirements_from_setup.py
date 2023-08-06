import re
import click

@click.command()
@click.option(
    "--input-file",
    required=True,
    help="The setup.py file to parse for requirements"
)
@click.option(
    "--output-file",
    default="requirements.txt",
    help="The file in which to write the extracted requirements"
)
def main(input_file, output_file):
    req_pattern = "requirements = \[(.*?)\]"
    with open(input_file, "r") as setup_file:
        data = setup_file.read().replace("\n", "")
    
    requirements = re.search(req_pattern, data).group(1).split()
    
    with open(output_file, "w") as req_file:
        for requirement in requirements:
            requirement = requirement.strip(",").replace('"', '')
            req_file.write(f"{requirement}\n")

if __name__ == "__main__":
    main()