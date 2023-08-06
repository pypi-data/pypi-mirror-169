#!/usr/bin/env python3
import json
import pathlib
from promptx import (
    PromptXCmdError,
    PromptXError,
    PromptXSelectError,
)
from typing import List
import sys
import shlex
import subprocess


class CommandError(Exception):
    """Exception raised when command fails"""

    def __init__(self, error, command, message="ERROR: Failed to run"):
        self.error = error
        self.message = message
        self.command = command

    def __str__(self):
        return f"{self.message} -> '{self.command}':\n{self.error}"


def ask(
    p,
    options: List,
    prompt=None,
    additional_args=None,
    select="first",
    deliminator="\n",
):
    try:
        choice = p.ask(
            options=options,
            prompt=prompt,
            additional_args=additional_args,
            select=select,
            deliminator=deliminator,
        )
    except (
        PromptXCmdError,
        PromptXError,
        PromptXSelectError,
    ) as err:
        print(err, file=sys.stderr)
        sys.exit(1)

    if not choice:
        print("No key, exiting", file=sys.stderr)
        sys.exit(1)

    return choice


def backup_file(original, backup):
    """
    Backup a file
    """
    o = pathlib.Path(original)
    if o.is_file():
        o.replace(backup)


def calc_lines(nkeys, columns):
    lines = 1 if (nkeys % columns) else 0
    while int(nkeys / columns):
        lines += int(nkeys / columns)
        nkeys %= columns
    return lines


def execute(cmd: str, shell: bool = False):
    command = cmd if shell else shlex.split(cmd)
    try:
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            shell=shell,
        )
    except subprocess.CalledProcessError as err:
        raise CommandError(err, command)
    return 0


def write_keys(user, keys, backup=True):
    if backup:
        backup_file(original=user.files["keys"], backup=user.files["keys_backup"])
    with open(user.files["keys"], mode="w") as data:
        json.dump(keys, data, indent=4)
