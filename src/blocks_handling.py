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

    # quote_bool = True
    # unord_list_bool = True
    # ord_list_bool = True
    # for i, line in enumerate(newlines_split):
    #     if not line.startswith('>'):
    #         quote_bool = False
    #     if not line.startswith('- '):
    #         unord_list_bool = False
    #     if not line.startswith(f'{i+1}. '):
    #         ord_list_bool = False
    # if quote_bool:
    #     return BlockType.QUOTE
    # if unord_list_bool:
    #     return BlockType.UNORDERED_LIST
    # if ord_list_bool:
    #     return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH