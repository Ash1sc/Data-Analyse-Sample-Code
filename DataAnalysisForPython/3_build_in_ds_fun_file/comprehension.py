import __init__
import numpy as np


if __name__ == "__main__":
    l = np.linspace(1, 30, 30)

    # comprehension for list
    new_l = [x for x in l if x % 6 == 0]

    # comprehension for nested lists, the order of for loop is the same with recursive for loop

    print(new_l)

    new_nested_l = [num for nums in l.reshape(5, 6) for num in nums if num % 6 == 0]
    print(new_nested_l)

    # comprehension in the comprehension
    new_nested_tup = [[t for t in tup] for tup in l.reshape(5, 6)]
    print(new_nested_tup)
