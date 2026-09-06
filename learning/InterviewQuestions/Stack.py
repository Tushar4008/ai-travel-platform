bracket_dict = {
                   ')':'(',
                   '}':'{',
                   ']':'[' 
                }

input_string= "([)"

def stack(bracket_dict,input_string):
    interim_list = []
    if len(input_string) == 1:
        return False 
    for char in input_string:
        if char not in bracket_dict:
            interim_list.append(char)
        else:
            l= len(interim_list)
            if l == 0:
                return False 
            if interim_list[-1] == bracket_dict[char]:
                interim_list.pop()
            else:
                return False

    if len(interim_list) == 0:
        return True
    else:
        return False 
    
print(stack(bracket_dict,input_string))

# for char in input_string:
#     if char in bracket_dict:
#         interim_list.append(char)
#     else:
#         key = next((k for k, v in bracket_dict.items() if v == char))
#         if interim_list[-1] == key:
#             interim_list.pop()


