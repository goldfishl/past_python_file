import sys
import os


def every_other(lst):
    """
    ([object]) -> ([object])
    >>> every_other([1, 2, 3, 4, 5])
    [1, 3, 5]
    """
    return lst[::2]


code = [chr(i) for i in range(97, 123)]
inv_code = code[::-1]
def solution(in_str):
    """
    >>> solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
    did you see last night's episode?

    >>> solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
    Yeah! I can't believe Lance lost his job at the colony!!
    """
    in_str = in_str.split()
    out_str = []
    for _str1 in in_str:
        _str2 = [ inv_code[code.index(ch)] \
                      if ch.islower() else ch for ch in _str1]
        out_str.append("".join(_str2))
    print(" ".join(out_str))


if __name__ == "__main__":
    print("Hello World")