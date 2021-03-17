from collections import deque

# -----------------宽度优先搜索---------------
# 需要定义好 graph
graph = {}
graph['a'] = ['b', 'c']

def Is_target(node):
    return node[-1] == 'm'

def breadth_firth_search(n):
    # 参数n为初始搜索节点
    searching = deque()
    searched = []

    searching += graph[n]
    while searching:
        node = deque.popleft()
        if node not in searching:
            if Is_target(node):
                print(f"{node} is target")
                return True
            else:
                searched.append(node)
                searching += graph[node]
    return False



    # -----------------------------快速排序-------------

    def quick_sort(arr):
        if len(arr) == 1:
            return arr
        else:
            mid = arr[0]
            low_arr = [i for i in arr[1:] if i < mid]
            great_arr = [i for i  in arr[1:] if i >=mid]
            return quick_sort(low_arr) + mid + quick_sort(great_arr)



# ---------------------------狄克斯特拉---------------------

# 定义图 graph 字典
# 定义cost 字典 初始只存放当前节点可以到达的cost，其他节点均为 float('inf)
# parents 存放父节点， 初始为空
# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"] = {}
graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"] = {}
graph["c"]["fin"] = 3
graph["c"]["d"] = 6

graph["d"] = {}
graph["d"]["fin"] = 1

graph["fin"] = {}


# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 5
costs["b"] = 2
costs["c"] = infinity
costs["d"] = infinity
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []# the parents table
def dijkstras_algorithm():
    node = find_low_cost()
    while node:
        neighbor = graph[node]
        for n in neighbor.keys():
            if neighbor[n] + costs[node] < costs[n]:
                costs[n] = neighbor[n] + costs[node]
                parents[n] = node
        processed.append(node)
        node = find_low_cost()

def find_low_cost():
    low_cost = float('inf')
    low_cost_node = None
    for n in costs:
        if n not in processed and costs[n] < low_cost:
            low_cost = costs[n]
            low_cost_node = n
    return low_cost_node



dijkstras_algorithm()
print(costs)