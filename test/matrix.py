import time
import os

import numpy
import pandas
from pathlib import Path


def create_matrix(rows: int, cols: int) -> numpy.ndarray:
    try:
        if rows <= 0 or cols <= 0:
            raise ValueError("Rows and columns must be greater than zero.")
        array = numpy.zeros((rows, cols))
        return array
    except ValueError as e:
        print(e)
        return None


def create_utmat(mat: numpy.ndarray) -> numpy.ndarray:
    rows, cols = mat.shape

    for i in range(rows):
        for j in range(cols):
            if i < j:
                mat[i, j] = 100
    return mat


def convert_df(points: list, mat: numpy.ndarray) -> pandas.DataFrame:
    df = pandas.DataFrame(mat)
    row_names = [f'{points[i]}' for i in range(len(points))]
    col_names = row_names

    df.index = row_names
    df.columns = col_names

    return df


def write_to_csv(output_dir, filename, df: pandas.DataFrame):
    if os.path.exists(output_dir):
        print("All good...")
    else:
        time.sleep(1.0)
        os.makedirs(output_dir)

    filepath = os.path.join(output_dir, filename)

    df.to_csv(filepath)
