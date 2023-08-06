#!/usr/bin/env python3
import os
from loadconf import Config
import pathlib
import sys

from .parser import batch_binds
from .options import get_opts
from .which import which_key


__license__ = "GPL-v3.0"
__program__ = "wkd"


def main():
    # Parse user args
    args = get_opts(__program__)
    # Create conf object and define files/settings
    user = Config(__program__)
    files = {
        "keys": "keys.json",
        "keys_backup": "old_keys.json",
        "conf": "wkdrc",
        "binds": "bindsrc",
    }
    settings = {
        "prompt_cmd": "dmenu",
        "bind_args": "",
        "separator": "->",
        "shell": False,
        "binds_dir": "binds",
        "keys_dir": "keys",
        "columns": 0,
    }
    create = ["conf", "keys", "keys_backup"]
    user.define_files(user_files=files)
    user.define_settings(settings=settings)
    user.create_files(create_files=create)
    user.read_conf(
        user_settings=list(settings.keys()),
        read_files=["conf"],
    )
    # User wants to read a different keys.json
    if args.read is not None:
        args.read = os.path.expanduser(args.read)
        # If not absolute path assume file is in $XDG_CONFIG_HOME
        if not os.path.isabs(args.read) and user.config_dir is not None:
            p = pathlib.Path(user.config_dir)
            args.read = str(p.joinpath(user.settings["keys_dir"], args.read))
        user.files["keys"] = args.read
    # Store keys
    user.store_files(
        files=["keys"],
        json_file=True,
    )
    # Format separator
    user.settings["separator"] = f" {user.settings['separator']} "
    if args.update:
        # Use different file as input if given
        if args.input is not None:
            args.input = os.path.expanduser(args.input)
            # If not absolute path assume file is in $XDG_CONFIG_HOME
            if not os.path.isabs(args.input) and user.config_dir is not None:
                p = pathlib.Path(user.config_dir)
                args.input = str(p.joinpath(user.settings["binds_dir"], args.input))
            user.files["binds"] = args.input
        # Use different file as output if given
        if args.output is not None:
            args.output = os.path.expanduser(args.output)
            # If not absolute path assume file is in $XDG_CONFIG_HOME
            if not os.path.isabs(args.output) and user.config_dir is not None:
                p = pathlib.Path(user.config_dir)
                args.output = str(p.joinpath(user.settings["keys_dir"], args.output))
            user.files["keys_backup"] = f"{args.output}.bak"
            user.files["keys"] = args.output
        # Store binds file
        user.store_files(files=["binds"])
        return batch_binds(user, args.debug)
    else:
        return which_key(user, keys=args.press)


if __name__ == "__main__":
    sys.exit(main())
