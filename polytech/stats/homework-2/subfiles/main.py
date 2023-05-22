import numpy as np
from part1 import part1
from part21 import part21
from part23 import part23
from part3 import part3

nums = []
with open('data.txt') as f:
    for line in f.readlines():
        nums.append(float(line))
data = np.array(nums)
rnd = int(100 * np.random.rand())
random_data = np.array(nums[rnd:rnd + 20])

part1(data)
part21(data, random_data)
part23(data, random_data)
part3(data)
