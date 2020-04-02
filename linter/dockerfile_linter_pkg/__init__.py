import sys
import os.path


def read_dockerfile(dockerfile_path):
    if not os.path.exists(dockerfile_path):
        print("FAIL    Specified Dockerfile doesn't exist!")
        sys.exit(1)

    filehandler = open(dockerfile_path, mode="r")
    lines = filehandler.readlines()
    filehandler.close()
    return lines


def lint(dockerfile_path):
    lines = read_dockerfile(dockerfile_path)
    print(lines)
