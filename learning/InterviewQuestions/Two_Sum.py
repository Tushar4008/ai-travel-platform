numbers = [2, 7, 8, 1]
final_list=[]
two_sum={}
target= 9 
for i in range(0,len(numbers)):
    required = target-numbers[i]
    if required in two_sum:
        required_index = two_sum.get(required)
        final_list.append([i,required_index])
    else:
        two_sum[numbers[i]]=i

print(final_list)

#target = 9

# two_sum=[]
# for i in range(0,len(numbers)):
#     for j in range(i+1,len(numbers)):
#         if numbers[i]+numbers[j] == 9:
#             two_sum.append([i,j])

# print(two_sum)


# final_list=[]

# # for i in range(0,len(numbers)-1):
# #     target_sum= numbers[i]+numbers[i+1]
# #     if target_sum == 9:
# #         final_list.append([i,i+1])


# # print(final_list)

# target_number=9
# numbers_dict=dict(enumerate(numbers))

# for i in range (0,len(numbers)):
#     number_difference= target_number-numbers[i]
#     if number_difference in numbers_dict:
#         final_list.append([i,next((k for k, v in numbers_dict.items() if v == number_difference), None)])

# print(final_list)