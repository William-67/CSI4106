weights = [1,2,3,4,5]
prices = [4156,489,321,489,6]
tmp_prices = [0,0,0,0,0]
tmp_weights = [0,0,0,0,0]
for i in range(len(prices)):
    tmp_prices[i] = prices[i]
    tmp_weights[i] = weights[i]

tmp_weights[3] = 1
print(tmp_weights)
print(weights)
