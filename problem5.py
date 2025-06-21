# Label the program written in problem 4 with comments.

import os

def list_directory_contents(path='.'):
    """
    Print all entries (files + dirs) in the specified directory.

    :param path: Directory path. Defaults to current working directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory {path!r} does not exist.")
        return
    except PermissionError:
        print(f"Error: Permission denied for directory {path!r}.")
        return

    print(f"Contents of {path!r}:")
    for name in entries:
        print(name)

if __name__ == '__main__':
    # List contents of current directory
    list_directory_contents()
    # Or pass a custom path:
    # list_directory_contents('/your/directory/here')
