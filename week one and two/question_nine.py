nums =  [2,7,11,15]
output = []
target = 9

for num in nums:
    difference = target - num
    if (difference in nums) and (difference != num):
        index_one = nums.index(num)
        index_two = nums.index(difference)
        
        output.append(index_one)
        output.append(index_two)
        
        nums.remove(num)

print(output)        
