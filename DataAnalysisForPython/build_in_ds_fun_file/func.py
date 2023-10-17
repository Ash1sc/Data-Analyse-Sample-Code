import __init__
import re
import itertools


def add_int(x: int, y: int, z: int = 3) -> None:
    '''
    keyword argument must follow the positonal argument
    '''
    print(x + y + z)


def remove_punctuation(value: str) -> str:
    return re.sub("[!#?]", "", value)


def cleaning_string(strings: list[str], ops):
    result = []
    for s in strings:
        for func in ops:
            s = func(s)

        result.append(s)
    return result


if __name__ == "__main__":

    add_int(1, 1)
    add_int(4, 3, 4)
    add_int(4, y=6)

    states = ["   Alabama ", "Georgia!", "Georgia", "georgia", "FlOrIda", "south   carolina##", "West virginia?"]

    # functino in python is an object, it's useful to use them to make a list of what you want to do to a set of data
    clean_ops = [str.strip, remove_punctuation, str.title]
    print([s for s in cleaning_string(states, clean_ops)])

    # Anonymous Function
    # for less typing in single-statement functions
    def apply_to_list(some_list: list[int], f):
        return [f(x) for x in some_list]
    l = [1, 2, 3, 4, 5]
    print(apply_to_list(l, lambda x: x*2))

    # or use map() to apply the function to each element within an iterable object
    print([i for i in map(lambda x: x*2, l)])

    # Generator
    # use () instead of [] in comprehension

    gen = (x**2 for x in range(100))
    print(sum(gen))

    # itertools module
    def len_mod_3(s: str):
        return len(s)
    clean_state = cleaning_string(states, clean_ops)
    print("\nGroupby example")
    # function return a tuple of index and grouper objects
    for _, names in itertools.groupby(clean_state, lambda s: len(s)):
        print(list(names))

    print("\nChain example")
    for name in itertools.chain(states, clean_state):
        print(name)

    print("\nCombination example")
    for name in itertools.combinations(clean_state, 6):
        print(name)

    # errors and exception handling
    def attempt_float(x):
        try:
            return float(x)
        except TypeError:
            return f"{x} cannot be convert to float"
        else:
            # the code here will only be executed when the code in try part is executed successfully
            pass
        finally:
            # the code here will be executed whether or not the code in try part is executed successfully
            pass

    print(attempt_float("1.2345"))
    print(attempt_float("something"))
