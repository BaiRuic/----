from collections import deque
from typing import List

graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ["anuj", "peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def preson_is_seller(name):
    return name[-1] == 'y'


def search(name:str):
    search_deque = deque()
    search_deque += graph[name]  # 维护一个队列
    searched = []     # 存放已经搜索过的
    while search_deque:
        preson = search_deque.popleft()
        if preson not in searched:
            if preson_is_seller(preson):
                print(f'The {preson} is a seller!')
                return True
            else:
                searched.append(preson)  # 将当前项加进以搜索过的列表
                search_deque += graph[preson] # 且将当前项指向的项目加进待搜索列表中
    return False

# 复习之前的 快速排序
def quick_sort(arr:List):
	if len(arr) <= 1:
		return arr
	else:
		mid = arr[0]
		less_arr = [i for i in arr[1:] if i <= mid]
		great_arr = [i for i in arr[1:] if i >mid]
		return quick_sort(less_arr) + [mid] + quick_sort(great_arr)

list = [545,23,1,76,34,23,78,45]

new_list = quick_sort(list)
print(new_list)

search('you')

