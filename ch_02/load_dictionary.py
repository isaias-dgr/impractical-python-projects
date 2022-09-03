import sys

def load(file):
    """Open a text file & retrun a list of lowercase strings."""

    try:
        with open(file, mode='r',encoding='UTF-8') as in_file:
            loaded_txt =  in_file.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as io_error:
        print(f"{io_error}\nError opening {sys.stderr}. Terminating program.")
        sys.exit(1)

        