#!/usr/bin/env python3

import os
import shutil
import argparse
import tempfile
from subprocess import check_call as call

MASTER_BRANCH = "master"
BUILD_BRANCH = "build"

REMOTE = "git@github.com:pektin/jam.git"
BUILD = os.path.join("build", "html")
REMOTE_SOURCE = os.path.join("source", "jam")

NO_DELETE = {
    ".git",
    ".nojekyll",
    "CNAME",
    "LICENSE",
    "README.md",
}

parser = argparse.ArgumentParser(prog="./build.py", description="Build script for lets-jam.org")
parser.add_argument(
    "-r", "--repo",
    type=str,
    help="The path to a clone of the jam repository. Used to fetch documentation.",
)
parser.add_argument(
    "action",
    choices=["build", "deploy"],
    help="What action to perform. Build does a sphinx build, while deploy also puts the build into a build branch.",
)


def main():
    args = parser.parse_args()

    # First switch to master branch
    call(["git", "checkout", MASTER_BRANCH])

    # Update the documentation copy
    if args.repo is None:
        with tempfile.TemporaryDirectory() as temp:
            call("git", "clone", REMOTE, temp)
            copy_docs(temp)
    else:
        copy_docs(args.repo)

    # Build docs
    call(["sphinx-build", "-b", "html", "source", BUILD])

    if args.action == "deploy":
        deploy()

def copy_docs(path):
    # First remove current docs copy if need be
    if os.path.isdir(REMOTE_SOURCE):
        shutil.rmtree(REMOTE_SOURCE)

    # Then copy new docs from path
    shutil.copytree(os.path.join(path, "docs"), REMOTE_SOURCE)

def deploy():
    # Copy build to a temporary directory
    with tempfile.TemporaryDirectory() as temp:
        print("Copying build to {}".format(temp))
        #temp = os.path.join("temp", "build")
        shutil.move(BUILD + "/", temp)

        # Change to build branch
        call(["git", "checkout", BUILD_BRANCH])

        # Remove all build files
        for file in os.listdir():
            if file not in NO_DELETE:
                if os.path.isdir(file):
                    shutil.rmtree(file)
                else:
                    os.remove(file)

        # Move new build
        path = os.path.join(temp, "html")
        for file in os.listdir(path):
            shutil.move(os.path.join(path, file), file)

if __name__ == "__main__":
    main()
