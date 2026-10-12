prices = [7,1,5,3,6,4]
# initial_difference = 0
# for i in range(0,len(prices)-1):
#     for j in range(i+1,len(prices)):
#         difference = prices[j]-prices[i]
#         if difference>initial_difference:
#             initial_difference = difference

# print(initial_difference)

profit=0
for i in range(0,len(prices)):
    if min_price>prices[i]:
        min_price=prices[i]

    max_profit = prices[i]-min_price
    if profit<max_profit:
        profit=max_profit

print(profit)