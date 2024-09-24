# Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordBank` array.
# You may reuse elements of `wordBank` as many times as needed.

# example:
# canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) -> true

# canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) -> false
# ska + t + ?
# sk + ate + boar + ?
# sk + ate _ bo + ?

# canConstruct("", ["cat", "dog", "mouse"]) -> true
# empty string generation takes 0 elements from the array

from typing import List


def can_construct(target: str, word_bank: List[str]) -> bool:
    if not target:
        return True

    for word in word_bank:
        index = target.find(word)
        if index == 0:
            suffix = target[len(word) :]
            if can_construct(suffix, word_bank):
                return True

    return False


if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # true
    print(can_construct("word", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))  # false
    print(
        can_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    )  # True
