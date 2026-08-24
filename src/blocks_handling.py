from enum import Enum
import re

def markdown_to_blocks(markdown):
    split_by_newline = markdown.split('\n\n')
    # print(f'1. markdown is split into {split_by_newline}')
    stripped_newlines = []
    for newline in split_by_newline:
        # print(f'2. iterating through "{newline}"')
        stripped_newline = newline.strip()
        # print(f'3. newline is stripped, now looks like: "{stripped_newline}"')
        if stripped_newline == '':
            continue
        stripped_newlines.append(stripped_newline)
    # print(f'4. finished iterating through list, final returned list = {stripped_newlines}')
    return stripped_newlines

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE

    lines = block.splitlines()

    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE

    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST
    
    if all(line.startswith(f'{i+1}. ') for i, line in enumerate(lines)):
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH