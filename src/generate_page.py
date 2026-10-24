import os

from blocks_handling import markdown_to_blocks
from markdown_to_html import markdown_to_html_node


def extract_title(markdown):
    """
    Function with the sole purpose of extracting the 
    text of header 1 of some markdown text.
    If no header is available, an exception is raised.
    """
    md_blocks = markdown_to_blocks(markdown)
    h1_capture = []
    for block in md_blocks:
        if block.startswith("# "):
            h1_capture.append(block)
    if h1_capture == []:
        raise ValueError("No title in markdown text")
    title = h1_capture[0]
    split_title = title.split(maxsplit=1)
    title_text = split_title[1]
    stripped_title_text = title_text.strip()
    return stripped_title_text

def generate_page(from_path, template_path, dest_path):
    """
    Function that generates an html file from a markdown file.
    Markdown file needs to be at the from path.
    Template needs populating with the template html to be populated by markdown.
    Destination needs specifying in the dest_path, inclusive of file name.
    Leverages the extract_title & markdown_to_html functions.
    """
    print(f"Using the markdown at {from_path} to generate html, insert into {template_path} and write to {dest_path}")
    
    with open(from_path, "rt") as f:
        md = f.read()

    node = markdown_to_html_node(md)
    html = node.to_html()
    title = extract_title(md)

    with open(template_path, "rt") as f:
        template = f.read()
    f.close()

    add_title = template.replace(r"{{ Title }}", title)
    add_content = add_title.replace(r"{{ Content }}", html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(add_content)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    """
    Function takes a directory path, recursively applies
    generate_page to every file to generate a linked up static site 
    in the specified directory.
    """
    if not os.path.isfile(dir_path_content):
        dir_path_list = os.listdir(dir_path_content)
        print(f"files in {dir_path_content}: {dir_path_list}")
        for dir in dir_path_list:
            sub_dir_path = dir_path_content + "/" + dir
            dest_sub_dir_path = dest_dir_path + "/" + dir
            generate_pages_recursively(sub_dir_path, template_path, dest_sub_dir_path)
    else:
        html_dest_dir_path = dest_dir_path.replace(".md", ".html")
        generate_page(dir_path_content, template_path, html_dest_dir_path)
