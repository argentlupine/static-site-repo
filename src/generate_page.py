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
    # notes!
    # Print a message confirming you are generating a web page
    # Read the markdown file at the from path
    # Use markdown to html node to convert the md to an html string
    # Use extract title to extract the title and store in a var
    # Replace the {{title}} and {{content}} variables in the template html
    # Write the full html page to a file at dest_path. 
    # Create any necessary directories if they don't exist.
    # 
    # Standard library options are:
    # open, .read(), .write(), .close(), .replace(), 
    # os.path.dirname, os.makedirs
    # fin
    print(f"Using the markdown at {from_path} to generate html, insert into {template_path} and write to {dest_path}")
    
    with open(from_path, "rt") as f:
        md = f.read()
    f.close()
    print(f"Extracted markdown {md}")

    html = markdown_to_html_node(md)
    print(f"Generated html {html}")

    title = extract_title(md)
    print(f"Extracted title {title}")

    with open(template_path, "rt") as f:
        template = f.read()
    f.close()
    print(f"Extracted template {template}")

    add_title = template.replace("{{ title }}", f"{{ {title} }}")
    add_content = add_title.replace("{{ content }}", f"{{ {html} }}")
    print(f"output prepped at {add_content}")

    # Now need to check dest path; if dir doesn't exist create
    os.makedirs(dest_path)
    with os.open(dest_path+"file.html", "x") as f:
        f.write(add_content)
    
    
    

