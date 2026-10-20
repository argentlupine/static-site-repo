def extract_title(markdown=str):
    """
    Function with the sole purpose of extracting the 
    text of header 1 of some markdown text.
    If a header isn't passed, an exception is raised.
    """
    if not markdown.startswith("# "):
        raise ValueError("Text passed is not the first Markdown header.")
    split_markdown = markdown.split(maxsplit=1)
    header_text = split_markdown[1]
    stripped_header_text = header_text.strip()
    return stripped_header_text
