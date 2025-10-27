from collections import Counter
from pprint import pprint

sentence = "The quick brown fox jumps over the lazy dog multiple times."

# Implementation : 1
# dict_counts = {}
# for char in sentence.lower():
#     if char == " ":
#         continue
#     elif char in dict_counts:
#         dict_counts[char] += 1
#     else:
#         dict_counts[char] = 1

# print(dict_counts)
# counter = -1
# for key, value in dict_counts.items():
#     if value > counter:
#         counter = value
#         most_frequent_char = key

# print(
#     f"The most frequent character is '{most_frequent_char}' with a count of {counter}.")

# Implementation : 2
# filtered = [ch for ch in sentence.lower() if ch.isalpha()]
# counts = Counter(filtered)
# pprint(counts)
# most_common_char, count = counts.most_common(1)[0]
# pprint(
#     f"The most frequent character is '{most_common_char}' with a count of {count}.")

# Implementation : 3
dict_counts = {}
for char in sentence.lower():
    if char == " ":
        continue
    elif char in dict_counts:
        dict_counts[char] += 1
    else:
        dict_counts[char] = 1

sorted_list = sorted(dict_counts.items(),
                     key=lambda item: item[1], reverse=True)
pprint(sorted_list[0])
