def solution(my_string):
    chars = []
    for char in my_string:
        if char not in chars:
            chars.append(char)
    answer = ''.join(chars)
    return answer

