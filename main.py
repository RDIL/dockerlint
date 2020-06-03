import os
import sys

if os.name == "nt":
    print("Exiting early - dockerlint is not supported on Windows yet!")
    sys.exit(0)

# import these after performing the windows check
import dockerfile_linter_pkg # noqa
import click # noqa


def report_all(issues, junit, dockerfile_path):
    """Reports the issue list."""

    for err in issues:
        click.secho("issue: " + str(err) + " ", fg="red")

    if junit:
        from dockerlint_xml_reporting import create_xml_report

        f = open("dockerlint.test_RESULTS.xml", "w")
        f.write(create_xml_report(issues, dockerfile_path))
        f.close()

    if len(issues) > 0:
        sys.exit(1)


@click.command()
@click.version_option(prog_name="dockerlint", version="0.2.1")
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
        dockerfile_linter_pkg.lint(dockerfile), report, dockerfile.name
    )


if __name__ == "__main__":
    main()
