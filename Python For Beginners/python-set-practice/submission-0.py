from typing import List

def contains_duplicate(words: List[str]) -> bool:
    first_word = words[0]
    for word in words[1:]:
        if word == first_word:
            return True

    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
