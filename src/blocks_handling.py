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