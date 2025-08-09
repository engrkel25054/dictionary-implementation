# Program specification
def get_min(d):
    """

    :param d: a dictionary that maps letters to integers.
    :return: the value in d with the key that occurs first in the alphabet. E.g. if d = {x: 11, b: 12,}, get_min(d) returns 12.
    """
    keys = []
    for key in d:
        keys.append(key)

    keys.sort()
    return d[keys[0]]


dict = {"x": 11, "b": 12, "y": 13, "z": 14, "a": 15}
print(get_min(dict))