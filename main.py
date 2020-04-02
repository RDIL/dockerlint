import sys
import dockerfile_linter_pkg


def find_dockerfile():
    dockerfile_at_index = None
    dockerfile_path = None

    for index, obj in enumerate(sys.argv):
        if "--dockerfile" in obj:
            dockerfile_at_index = index + 1

        if (
            dockerfile_at_index is not None
            and index == dockerfile_at_index
        ):
            dockerfile_path = obj

    return dockerfile_path if dockerfile_path is not None else "Dockerfile"


def main():
    print("\nStarting dockerlint...\n")
    the_path = find_dockerfile()
    print("INFO    Using dockerfile from path: " + the_path)
    dockerfile_linter_pkg.lint(the_path)


if __name__ == "__main__":
    main()
