import os
import sys

if os.name == "nt":
    print("Exiting early - dockerlint is not supported on Windows yet!")
    sys.exit(0)

import dockerfile_linter_pkg
import click


def report(issues):
    """Reports the issue list."""

    for err in issues:
        final_string = click.style("issue: " + str(err) + " ", fg="red")
        final_string = final_string + click.style(
            err.id, fg="red", underline=True
        )
        click.echo(final_string)

    if len(issues) > 0:
        sys.exit(1)


@click.command()
@click.option(
    "--dockerfile",
    "-d",
    required=True,
    type=click.File("r"),
    help="The Dockerfile to lint.",
)
def main(dockerfile):
    """Run dockerlint."""

    click.secho("\n    Starting dockerlint...\n", bold=True, fg="cyan")
    click.secho(
        "info: Using dockerfile from path: " + dockerfile.name, fg="blue"
    )
    report(dockerfile_linter_pkg.lint(dockerfile))


if __name__ == "__main__":
    main()
