#!/usr/bin/env python3
import sys
from promptx import (
    PromptX,
    PromptXCmdError,
    PromptXError,
    PromptXSelectError,
)
from .utils import CommandError, calc_lines, execute


def ask_loop(prompt_x, keys, shell, columns):
    """
    Show user keys at current level.
    """
    p = prompt_x
    options = keys.keys()
    args = ""
    if columns:
        nkeys = len(options)
        lines = calc_lines(nkeys=nkeys, columns=columns)
        args = f"-g {columns} -l {lines}"
    try:
        bind = p.ask(options=options, additional_args=args)
    except (
        PromptXCmdError,
        PromptXError,
        PromptXSelectError,
    ) as err:
        print(err, file=sys.stderr)
        return 1
    if bind is None:
        return 1
    if isinstance(keys[bind], dict):
        ask_loop(
            prompt_x=p,
            keys=keys[bind],
            shell=shell,
            columns=columns,
        )
    else:
        try:
            return execute(keys[bind], shell=shell)
        except CommandError as err:
            print(err, sys.stderr)
            return 1
    return 0


def press_key(keys, press_keys):
    """
    Press the keys provided by -p
    """
    if not press_keys:
        return keys
    pop_key = None
    for key in keys:
        if key.startswith(press_keys[0]):
            pop_key = key
    if pop_key:
        keys = keys[pop_key]
        del press_keys[0]
    if press_keys:
        return press_key(keys=keys, press_keys=press_keys)
    return keys


def which_key(user, keys):
    """
    Show user a list of keybinds defined for wkd
    """
    p = PromptX(
        prompt_cmd=user.settings["prompt_cmd"],
        default_args=user.settings["bind_args"],
    )
    press_keys = None
    if keys:
        press_keys = []
        press_keys.extend(keys)
    keys = press_key(keys=user.stored["keys"], press_keys=press_keys)
    columns = user.settings["columns"]
    return ask_loop(
        prompt_x=p,
        keys=keys,
        shell=user.settings["shell"],
        columns=columns,
    )
