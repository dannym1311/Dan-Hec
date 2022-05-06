
def singleNumber(nums: list[int]) -> int:
    counts = {}
    for number in nums:
        if number in counts.keys():
            counts[number] += 1
        else:
            counts[number] = 1
    for (number, count) in counts.items():
        if count == 1:
            return number

print(singleNumber([4,1,2,1,2]))


print(singleNumber([4,3,3,5,4,1,1]))











