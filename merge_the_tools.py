def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        temp_string = string[i:i+k]
        sub_string = ''
        for j in temp_string:
            if j not in sub_string:
                sub_string += j
        print(sub_string)

merge_the_tools('AABCAAADA', 3)