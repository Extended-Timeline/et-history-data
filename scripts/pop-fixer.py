'''
Created on 27.11.2025

@author: thetraveller60
'''
import os
import re

locations_folder = "../locations/"

#yml block template :3
DATE_RE = re.compile(r'^(\S+):\s*$')


def extract_date_blocks(lines):
    """uhh identify blocks."""
    blocks = []
    current_key = None
    start = None

    for i, line in enumerate(lines):
        m = DATE_RE.match(line)
        if m:
            if current_key is not None:
                blocks.append((current_key, lines[start:i], start, i))
            current_key = m.group(1)
            start = i

    if current_key is not None:
        blocks.append((current_key, lines[start:], start, len(lines)))

    return blocks


def fix_pops_in_block(block):
    """fix pops formatting."""
    text = "".join(block)

    # find pops
    pops_header = re.search(r'^(\s*)pop:\s*$', text, re.MULTILINE)
    if not pops_header:
        return block, False

    indent = pops_header.group(1)

    # collect pops
    lines = text.splitlines(keepends=True)
    pops_body = []
    start_collecting = False

    for line in lines:
        if not start_collecting:
            if re.match(r'^' + re.escape(indent) + r'pop:\s*$', line):
                start_collecting = True
            continue
        else:
            if re.match(r'^' + re.escape(indent) + r'\S', line):
                break
            pops_body.append(line)

    # extract individual pops
    entries = []
    current = {}

    for line in pops_body:
        m = re.match(r'^\s+(\S+):\s*(.*)$', line)
        if m:
            key = m.group(1)
            val = m.group(2)
            if key in current:
                entries.append(current)
                current = {}
            current[key] = val

    if current:
        entries.append(current)

    # build corrected pops list
    new_pops = indent + "pops:\n"
    for entry in entries:
        new_pops += indent + "  - "
        first = True
        for k, v in entry.items():
            if first:
                new_pops += f"{k}: {v}\n"
                first = False
            else:
                new_pops += indent + f"    {k}: {v}\n"

    # replace old pops list
    pops_full_re = re.compile(
        r'^' + re.escape(indent) + r'pop:\s*\n(?:' +
        r'(?:\s+.*\n)+' +
        r')',
        re.MULTILINE
    )

    new_block = pops_full_re.sub(new_pops, text)

    return new_block.splitlines(keepends=True), True


def add_default_pop(block):
    """add a default pop lol."""
    lines = block
    first_line = lines[0]
    indent = re.match(r'^(\s*)', first_line).group(1)
    add_indent = indent + "  "

    new_block = [
        lines[0],
        f"{add_indent}pops:\n",
        f"{add_indent}  - religion: missing_religion\n",
        f"{add_indent}    culture: missing_culture\n",
        f"{add_indent}    estate: peasant\n",
        f"{add_indent}    size: 1000\n",
    ] + lines[1:]

    return new_block


# ---------------------------------------------
# MAIN SCRIPT
# ---------------------------------------------
for root, dirs, files in os.walk(locations_folder):
    for file in files:
        if not file.endswith(".yml"):
            continue

        location_file = os.path.join(root, file)
        print("Processing:", file)

        with open(location_file, 'r') as f:
            lines = f.readlines()

        blocks = extract_date_blocks(lines)
        modified = False
        new_lines = list(lines)

        for idx in reversed(range(len(blocks))):
            key, block, start, end = blocks[idx]

            fixed_block, has_pops = fix_pops_in_block(block)

            if not has_pops and idx == 0:
                fixed_block = add_default_pop(block)
                has_pops = True

            if fixed_block != block:
                modified = True

            new_lines[start:end] = fixed_block

        if modified:
            with open(location_file, 'w') as f:
                f.writelines(new_lines)
            print("--> Fixed:", file)
        else:
            print("--> No changes!!")
