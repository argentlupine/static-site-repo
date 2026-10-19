import os
import shutil


def copy_files_to_public_directory(source_directory, public_directory):
    """
    Recursive function that copies files from a source directory to a public
    directory. It does the following:
    - Deletes contents of the public directory
    - Copies all files, subdirectories, nested files etc. from static to public
    """
    if os.path.exists(public_directory):
        shutil.rmtree(public_directory)
    os.mkdir(public_directory)
    directory_loop(source_directory, public_directory)

def directory_loop(source, public):
    """
    Support function for copy_files_to_public_directory
    Recursively loops through a directory, and copies files to the 
    public directory with the same relative path.
    Accepts arguments:
    - source: the path in source to be looped through.
    - public: the corresponding destination files will be copied to.
    """
    print(f"Log: looping through {source}")
    dir_list = os.listdir(source)
    for entry in dir_list:
        source_path = os.path.join(source, entry)
        print(f"Log: assessing {source_path}")
        if not os.path.isfile(source_path):
            new_public_dir = os.path.join(public, entry)
            os.mkdir(new_public_dir)
            print(f"Log: replicated directory {entry} in {new_public_dir}")
            directory_loop(source_path, new_public_dir)
        else:
            public_filepath = os.path.join(public, entry)
            shutil.copy(source_path, public_filepath)
            print(f"Log: copied {entry} to {public_filepath}")

if __name__ == "__main__":
    source_directory = "./static"
    public_directory = "./public"
    copy_files_to_public_directory(source_directory, public_directory)
