#!/usr/bin/env python3
import json
import re
import sys
from .utils import write_keys


def batch_binds(user, debug=False):
    """
    Add user binds from a batch file
    """
    binds_dict = generate_binds(
        binds=user.stored["binds"],
        separator=user.settings["separator"],
    )
    if binds_dict is None:
        print("ERROR: Malformed batch_binds.conf", file=sys.stderr)
        return 1
    if debug:
        binds = json.dumps(binds_dict, indent=4)
        print(binds)
    else:
        write_keys(user=user, keys=binds_dict)
    return 0


def generate_binds(binds, separator):
    """
    Generate binds from user given file
    """
    # Create regex objects for getting valuable info
    full_regx = re.compile(r"^:+")
    prefix_regx = re.compile(r"\s*==.*$")
    command_regex = re.compile(r"^.*?==")
    separator_regex = re.compile(r"(^.)\s+")
    exit_regex = re.compile(r"^.\S")
    # Create some blank storage devices Store the prefixes above the current
    # level
    prefix_list = []
    # Store all binds here, update after each loop where a command is found
    binds_dict = {}
    # Store subprefixes, cleared after each loop
    temp_dict = {}
    # Start at level 0
    level = 0
    # prev_level is how far down we have gone. Allows for maintaining prefix
    # bounds
    prev_level = 0
    for bind in binds:
        # Clean line of left white space
        bind = bind.lstrip()
        # If line is a comment skip
        if bind.startswith("#"):
            continue
        # Get the full_line without ":"
        full_line = full_regx.sub("", bind)
        # Test if line is formated correctly if poorly formated stop
        exit_match = exit_regex.match(full_line)
        if exit_match:
            binds_dict = None
            break
        # Add separator
        full_line = separator_regex.sub(rf"\1{separator}", full_line)
        # Get command if given, else this will equal full_line
        command = command_regex.sub("", full_line)
        # Get a match for the number of ":"
        level_match = full_regx.match(bind)
        # Set level to number of matches if found else 0
        level = level_match.end() if level_match else 0
        # If level is 0 reset everything
        temp_dict = {}
        # If level is deeper than previous update prev_level
        if level > prev_level:
            prev_level = level
        # If level is above previous level clear out the last n prefixes to get
        # on same level
        elif level < prev_level and prefix_list:
            up = prev_level - level
            prev_level = level
            for _ in range(up):
                del prefix_list[-1]
        # If command and full_line are the same then store the prefix and continue
        if command == full_line:
            prefix_list.append(full_line)
            continue
        # We have found a command, time for the heavy lifting
        else:
            # Get the bind plus description for the command
            keybind = prefix_regx.sub("", full_line)
            # Cleanup the command
            command = command.strip()
            # Create the terminating dict
            temp_dict[keybind] = command
            # Get dict based on prefixes
            temp_dict = prefixer(
                prefix_list=prefix_list,
                command_dict=temp_dict,
                index=0,
            )
            # Update binds_dict
            # binds_dict = update_binds(binds_dict, temp_dict)
            update_binds(binds_dict, temp_dict)
    return binds_dict


def prefixer(
    prefix_list,
    command_dict,
    index,
):
    """
    Recursively get a prefix dict from a prefix list
    """
    # If prefix_list is empty return the command_dict
    if not prefix_list:
        return command_dict
    # Clear out values
    temp_dict = {}
    return_dict = {}
    # If we have not reached the end of the list incriment the index and go a
    # level deeper
    if index < len(prefix_list) - 1:
        index += 1
        temp_dict = prefixer(
            prefix_list=prefix_list,
            command_dict=command_dict,
            index=index,
        )
        command_dict = temp_dict
    if temp_dict:
        index -= 1
    return_dict[prefix_list[index]] = command_dict
    return return_dict


def update_binds(dict1, dict2):
    """
    Update binds_dict given temp_dict
    """
    for key1, val in dict1.items():
        # If val is a dict, we need to check if it exists and is a dict in dict2
        if isinstance(val, dict):
            # If it is a dict and is in dict2, dive deeper
            if key1 in dict2 and isinstance(dict2[key1], dict):
                # Update dict1
                update_binds(dict1[key1], dict2[key1])
        else:
            # Else if key1 is in dict2 but not a dict update the value
            if key1 in dict2:
                dict1[key1] = dict2[key1]

    # Check the dict2
    for key2, val in dict2.items():
        # If key2 is not in dict1 and val is not equal to dict1
        # check the key
        if not key2 in dict1 and val != dict1:
            # Get the keybind
            k = re.sub(r"(^.).*$", r"\1", key2)
            found = False
            pop_key = None
            # Check to see if keybind is in dict1
            for key1 in dict1.keys():
                # If it is we remove it
                if key1.startswith(k):
                    found = True
                    pop_key = key1
                    break
            if found:
                dict1.pop(pop_key, None)
            dict1[key2] = val
    # return dict1
