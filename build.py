#!/usr/bin/env python3

import os
from os import path
import shutil
import argparse
import tempfile
from subprocess import check_call as call

SOURCE_BRANCH = "site"
BUILD_BRANCH = "master"

REMOTE = "git@github.com:pektin/jam.git"
DOCS_PATH = "docs"
SOURCE_DOCS_PATH = path.join("source", "docs")
BUILD_PATH = path.join("build", "html")

parser = argparse.ArgumentParser(prog="./build.py", description="Build script for lets-jam.org")
parser.add_argument(
    "-r", "--repo",
    type=str,
    help="The path to a clone of the jam repository. Used to fetch documentation.",
)
parser.add_argument(
    "action",
    choices=["build", "deploy", "clean"],
    help="What action to perform. Build does a sphinx build, while deploy also puts the build into a build branch.",
)


def main():
    args = parser.parse_args()

    if args.action == "clean":
        shutil.rmtree("build")
        return

    # Update the documentation copy
    if args.repo is None:
        with tempfile.TemporaryDirectory() as temp:
            call(["git", "clone", REMOTE, temp])
            copy_docs(temp)
    else:
        copy_docs(args.repo)

    # Build docs
    call(["sphinx-build", "-b", "html", "source", BUILD_PATH])

    if args.action == "deploy":
        deploy()

def copy_docs(docs_path):
    # First remove current docs copy if need be
    if path.isdir(SOURCE_DOCS_PATH):
        shutil.rmtree(SOURCE_DOCS_PATH)

    # Then copy new docs from path
    shutil.copytree(path.join(docs_path, DOCS_PATH), SOURCE_DOCS_PATH)

def deploy():
    # Copy build to a temporary directory
    with tempfile.TemporaryDirectory() as temp:
        print("Copying build to {}".format(temp))
        shutil.move(path.join(BUILD_PATH, ""), temp)

        # Change to build branch
        call(["git", "checkout", BUILD_BRANCH])

        # Remove all build files
        for file in os.listdir():
            if file == ".git": continue
            if path.isdir(file):
                shutil.rmtree(file)
            else:
                os.remove(file)

        # Move new build
        html_path = path.join(temp, "html")
        for file in os.listdir(html_path):
            shutil.move(path.join(html_path, file), file)

if __name__ == "__main__":
    main()
