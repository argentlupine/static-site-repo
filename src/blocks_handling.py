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
    # Identify header
    header_split = block.split(maxsplit=1)
    if re.fullmatch(r'#+', header_split[0]):
        return BlockType.HEADING
    
    newlines_split = block.splitlines(keepends=True)
    # print(f'newlines split looks like: {newlines_split}')

    # print(f'code split looks like: {code_split}')
    if newlines_split[0] == "```\n" and newlines_split[-1] == "```":
        return BlockType.CODE

    # Identify quotes, unordered and ordered lists
    quote_bool = True
    unord_list_bool = True
    ord_list_nums = []
    for line in newlines_split:
        if line[0] != '>':
            quote_bool = False
        if line[0:2] != '- ':
            unord_list_bool = False
        first_space_split = line.split(maxsplit=1)
        if re.fullmatch(r'[0-9]+\.', first_space_split[0]):
            ord_list_nums.extend(re.findall(r'([0-9]+)', first_space_split[0]))
            # print(f'appended {first_space_split[0]} to ord_list_nums')
    if quote_bool:
        return BlockType.QUOTE
    if unord_list_bool:
        return BlockType.UNORDERED_LIST
    # print(f'final ordered list check is {ord_list_nums}')
    # print(f'the first item is {ord_list_nums[0]}')
    order_copy = ord_list_nums.copy()
    order_copy.sort()
    # print(f'if the ordered list is sorted: {order_copy}')
    if ord_list_nums[0] == '1' and \
        ord_list_nums == order_copy:
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH