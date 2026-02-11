# text = "aabbccc"
#
# freq = {}
# for char in text:
#     freq[char] = freq.get(char, 0) + 1
#
# freq_of_freq = {}
# for value in freq.values():
#     freq_of_freq[value] = freq_of_freq.get(value, 0) + 1
#
# print("частоты:", freq)
# print("частота частот:", freq_of_freq)

#2
# numbers = [1, 3, 2, 4, 3]
#
# def is_zigzag(arr):
#     if len(arr) < 2:
#         return True
#
#     up = arr[0] < arr[1]
#     down = arr[0] > arr[1]
#
#     for i in range(1, len(arr) - 1):
#         if up and not (arr[i] > arr[i+1]):
#             up = False
#         if down and not (arr[i] < arr[i+1]):
#             down = False
#
#     return up or down
#
#
# print("зигзаг:", is_zigzag(numbers))

#3
# user1 = {"Alice", "Bob", "Charlie"}
# user2 = {"Bob", "Diana", "Eve"}
#
# result = user1 ^ user2
#
# print(result)



