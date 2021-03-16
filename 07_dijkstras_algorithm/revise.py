from collections import deque
# ---------------宽度优先搜索---------------

# 构件图
graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def Is_target(x:str):
    return x[-1] == 'k'

def breadth_search(x:str):
    searching = deque()
    searching += graph[x]
    searched = []

    while searching:
        person = searching.popleft()
        if person not in searched:
            if Is_target(person):
                print(f"{person} is the target")
                return True
            else:
                searched.append(person)
                searching += graph[person]
    print('Not find')
    return False

# ------------------快速排序------------------

def quick_sort(arr):
    if len(arr) <= 1 :
        return arr
    else:
        mid = arr[0]
        less_arr = [i for i in arr[1:] if i <= mid ]
        great_arr = [i for i in arr[1:] if i > mid]
        return quick_sort(less_arr) + [mid] + quick_sort( great_arr)



# -----------------使用递归来求数组和-----------
def quick_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

# ------------------执行-----------------------
breadth_search('you')  

list = [34,2,13,56,32,78,13,122,45]
after_sort = quick_sort(list)
print(after_sort)  

sum = quick_sum(list)
print(sum)





