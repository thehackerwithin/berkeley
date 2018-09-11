import os
import sys

import nbformat
import nbconvert.preprocessors


def main(NOTEBOOK_PATHS):
    for notebook_path in NOTEBOOK_PATHS:
        do_preprocessing(notebook_path, notebook_path)


def do_preprocessing(notebook_path, output_path):

    output_directory = os.path.dirname(output_path)
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    print("Clearing {0}".format(notebook_path))

    preprocessor = nbconvert.preprocessors.ClearOutputPreprocessor()
    preprocessor.preprocess(nb, {'metadata': {'path': output_directory}})

    with open(output_path, 'wt') as f:
        nbformat.write(nb, f)

    print("\tSaved to {0}".format(output_path))


if __name__ == "__main__":
    NOTEBOOK_PATHS = sys.argv[1:]
    sys.exit(main(NOTEBOOK_PATHS))
