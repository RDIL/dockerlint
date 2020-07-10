import os
import sys

if os.name == "nt":
    print("Exiting early - dockerlint is not supported on Windows yet!")
    sys.exit(0)

# import these after performing the windows check
from . import linter  # noqa
import click  # noqa


def report_all(issues, junit, dockerfile_path):
    """Reports the issue list."""

    for err in issues:
        click.secho("issue: " + str(err) + " ", fg="red")

    if junit:
        from . import xml_reporting

        f = open("dockerlint.test_RESULTS.xml", "w")
        f.write(xml_reporting.create_xml_report(issues, dockerfile_path))
        f.close()

    if len(issues) > 0:
        sys.exit(1)


@click.command()
@click.version_option(prog_name="dockerlint", version="0.3.1")
@click.option(
    "--dockerfile",
    "-d",
    required=True,
    type=click.File("r"),
    help="The Dockerfile to lint.",
)
@click.option(
    "--report",
    "-R",
    is_flag=True,
    default=False,
    help="Output a JUnit report of the tests.",
)
def main(dockerfile, report):
    """Run dockerlint."""

    click.secho("\n    Starting dockerlint...\n", bold=True, fg="cyan")
    click.echo("Using dockerfile from path: " + dockerfile.name)
    report_all(
        linter.lint(dockerfile), report, dockerfile.name
    )


if __name__ == "__main__":
    main()
