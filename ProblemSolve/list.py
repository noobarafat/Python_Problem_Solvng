nums = [23, 34, 45, 565, 645, 'Arafat']

print(nums[3])
print(nums[2:])
print(nums[-1])


names = ['Arafat', 'Zia', "Juthy"]
print(names)

values = [9.5,'Data', 56]
print(values)

mil = [nums, names]
print(mil)

nums.append(45)
print(nums)

# nums.clear()
# print(nums)

nums.insert(2, 'zia')
print(nums)

nums.remove(23)
print(nums)

nums.pop(1)
print(nums)

nums.pop()
print(nums)

del nums[2:4]
print(nums)

# del nums[1:]
# print(nums)

nums.extend([12, 'Rafique', 45, 566])
print(nums)

nums.remove('Arafat')
nums.remove('Rafique')

min_num = min(nums)
print(min_num)
print(max(nums))
print(sum(nums))


