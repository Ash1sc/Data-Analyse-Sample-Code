import __init__
import numpy as np


if __name__ == "__main__":
    data = np.array([[1.5, -0.1, 3.], [0., -3, 6.5]])

    # Arrays can enble us to apply simple operations to the data in the whole ndarray at the same time
    print(data)
    print(data * 2)
    print(data + data)

    # print ndarray metadata
    print(f"data.shape is {data.shape}")
    print(f"data's type is {data.dtype}")
    print(f"data has {data.ndim} dimensions")\

    # create ndarray
    # from sequential-like list

    # array
    arr1 = np.array([6, 7.5, 8, 0, 1])
    # nested array
    arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    # from build-in functions for special ndarray
    arr_zeros = np.zeros(10)
    arr_zeros2 = np.zeros((3, 6))

    arr_one = np.ones((3, 6))

    # initial the array without initial the data inside is dangerous!
    arr_empty = np.empty((3, 6))

    arr_full = np.full((3, 6), 5)

    # change dtype
    arr = np.array([1, 2, 3, 4, 5])
    arr2 = arr.astype(np.float64)

    # * Arithmetic with NumPy Arrays
    # Any arithmetic or Comparison operations between equal-size arrays apply the operation element-wise
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(arr * arr)
    print(arr - arr)

    # Arithemetic with scalars propagate the scalar argument to each element in the array
    print(1 / arr)

    # * Basic Indexing and Slicing

    # one-dimention array
    arr = np.arange(10)

    # single element
    print(arr[5])
    # subset
    print(arr[5:8])

    # mutation of subset will reflected to the orignal arrays
    print(arr)
    sub = arr[5:8]
    sub[:] = 1000
    print(sub)
    print(arr)

    # want to copy a array
    sub = arr[5:8].copy()

    # multi-dimention array
    arr2d = np.arange(30).reshape([5, 6])

    # get an element
    print(arr2d[1][2])
    print(arr2d[2, 3])

    # get a subset
    print(arr2d[1:][:2])

    # Boolean Indexing

    

