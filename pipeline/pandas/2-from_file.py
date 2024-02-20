import pandas as pd

def from_file(filename, delimiter):
    """
    Loads data from a file into a pandas DataFrame.

    Args:
        filename (str): The file to load from.
        delimiter (str): The column separator.

    Returns:
        pd.DataFrame: The loaded DataFrame.
    """
        # Load data from file into DataFrame
    df = pd.read_csv(filename, delimiter=delimiter)
    return df