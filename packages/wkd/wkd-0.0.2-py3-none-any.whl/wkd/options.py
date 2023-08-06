#!/usr/bin/env python3
import argparse


def get_opts(prog_name="wdk"):
    parser = argparse.ArgumentParser(
        prog=prog_name,
        description="""
        Which-key via dmenu.
        """,
        allow_abbrev=False,
    )
    group = parser.add_mutually_exclusive_group()
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="""
        Instead of (re)writing your keys.json when updating prints to screen.
        """,
    )
    parser.add_argument(
        "-i",
        "--input",
        metavar="FILE",
        action="store",
        default=None,
        help="""
        Can be used with --update to read a different bindsrc file.
        """,
    )
    parser.add_argument(
        "-o",
        "--output",
        action="store",
        default=None,
        metavar="FILE",
        help="""
        Can be used with --update to output to a different keys.json file.
        """,
    )
    parser.add_argument(
        "-p",
        "--press",
        action="store",
        default=None,
        metavar="KEY(s)",
        help="""
        Effectively presses KEY(s) after launching.
        """,
    )
    group.add_argument(
        "-r",
        "--read",
        action="store",
        metavar="FILE",
        default=None,
        help="""
        Read an alternate keys.json file. If FILE is a relative path wkd assumes
        it is in the $XDG_CONFIG_HOME/wkd/keys directory.
        """,
    )
    group.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="""
        Update keybinds using bindsrc. See --input and --output for additional options.
        """,
    )
    args = parser.parse_args()
    return args
