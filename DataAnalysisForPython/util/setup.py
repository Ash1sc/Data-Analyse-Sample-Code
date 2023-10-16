import pandas as pd
import numpy as np


def beatify_output() -> None:
    pd.options.display.max_columns = 20
    pd.options.display.max_rows = 20
    pd.options.display.max_colwidth = 80
    np.set_printoptions(precision=4, suppress=True)
    print("This is not main")
