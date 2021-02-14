def make_pi():
    return [3,1,4]


def common_end(a, b):
    return a[0] == b[0] or (a[-1] == b[-1])


def sum3(nums):
    sums = 0
    for i in nums:
        sums += i
    return sums


def rotate_left3(nums):
    return nums[1:]+nums[0:1]


def reverse3(nums):
    return nums[::-1]


def max_end3(nums):
    if nums[0]>nums[-1]:
        return [nums[0] for _ in range(len(nums))]
    else:
        return [nums[-1] for _ in range(len(nums))]


def sum2(nums):
    if len(nums) > 1:
        sums = nums[0] + nums[1]
    elif len(nums) == 1:
        sums = nums[0]
    else:
        sums = 0
    return sums


def middle_way(a, b):
    return [a[1],b[1]]


def make_ends(nums):
    return [nums[0],nums[-1]]


def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False

def check(array, target):
    oc = array.count(1)
    for x in range(len(array) - 1):
        if array[x] == 0:
            if array[x - 1] == 0 and array[x + 1] == 0:
                array[x] = 1
    fc = array.count(1)
    print(array)
    if fc - oc == target:
        return True
    else:
        return False

print(check([0,1,0,0,0,0,0,1],2))


