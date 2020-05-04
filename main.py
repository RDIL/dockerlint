import os
import sys
import dockerfile_linter_pkg
import click

if os.name == "nt":
    print("Exiting early - dockerlint is not supported on Windows yet!")
    sys.exit(0)


def report_all(issues, junit, dockerfile_path):
    """Reports the issue list."""

    for err in issues:
        final_string = click.style("issue: " + str(err) + " ", fg="red")
        final_string = final_string + click.style(
            err.id, fg="red", underline=True
        )
        click.echo(final_string)

    if junit:
        from dockerlint_xml_reporting import create_xml_report

        f = open("dockerlint.test_RESULTS.xml", "w")
        f.write(create_xml_report(issues, dockerfile_path))
        f.close()

    if len(issues) > 0:
        sys.exit(1)


@click.command()
@click.version_option(prog_name="dockerlint", version="0.1.0")
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
    click.secho(
        "info: Using dockerfile from path: " + dockerfile.name, fg="blue"
    )
    report_all(
        dockerfile_linter_pkg.lint(dockerfile), report, dockerfile.name
    )


if __name__ == "__main__":
    main()
