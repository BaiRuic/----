from typing import List


# 快速排序
def quicksort(arr:List):
    if len(arr) < 2:    # 基线条件
        return arr
    else:    # 递归条件
        mid = arr[0]    # 随便找一个基准 
        less = [i for i in arr[1:] if i <= mid] # 小于基准的元素
        greet = [i for i in arr[1:] if i > mid] # 大于基准的元素
        return quicksort(less) + [mid] + quicksort(greet) # 分而治之的思想  ：把小于基准的元素和大于基准的元素 分别再递归调用 该函数 实现排序


# 使用递归 求列表元素之和
def recursion_sum(arr:List):
    if len(arr) < 1:
        return 0
    else:
        return arr[0] + recursion_sum(arr[1:]) 


# 使用递归来计算数组元素个数：
def recursion_len(arr:List):
    if arr == []:
        return 0
    else:
        return 1 + recursion_len(arr[1:])

# 使用递归来计算数组最大值
def recursion_max(arr:List):
    if len(arr) <= 1:
        return arr[0]
    else :
        max = arr[0]
    return max if max > recursion_max(arr[1:]) else recursion_max(arr[1:])


arr = [3,6,1,78,23,98,0,2,23,1,99]

print(f"元素个数{recursion_len(arr)}")
print(f"快速排序：{quicksort(arr)}")
print(f"最大值{recursion_max(arr)}")
print(f"元素和{recursion_sum(arr)}")


