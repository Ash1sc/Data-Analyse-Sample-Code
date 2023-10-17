from typing import Any
import pandas as pd
import numpy as np


def beatify_output() -> None:
    pd.options.display.max_columns = 20
    pd.options.display.max_rows = 20
    pd.options.display.max_colwidth = 80
    np.set_printoptions(precision=4, suppress=True)
    print("this is not main")


class c:
    def __init__(self, i: int = 1) -> None:
        self.attr: int = i

    def __str__(self) -> str:
        return f"The value of attr is {self.attr}"
        return "The value of attr is {}".format(self.attr)

    def get_attr(self) -> int:
        return self.attr

    def set_attr(self, new_i) -> None:
        self.attr = new_i
