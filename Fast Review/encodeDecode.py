def encode(self, strs):
    # write your code here
    # put length of word and delimiter in front of each string
    result = ""
    for word in strs:
        result += str(len(word)) + "#" + word
    return result


"""
@param: str: A string
@return: dcodes a single string to a list of strings
"""


def decode(self, str):
    # write your code here
    # Algorithm: store int values till the first # then splice the string by that many characters
    decoded, index = [], 0
    while index < len(str):
        j = index
        while str[j] != "#":
            j += 1
        length = int(str[index:j])
        decoded.append(str[j + 1:j + 1 + length])
        index = j + 1 + length
    return decoded
