# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []# the parents table

# 在costs表格中查找代价最低的节点
def find_low_cost(costs):
    low_cost = float('inf')
    low_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < low_cost and node not in processed:
            low_cost = cost
            low_cost_node = node
    return low_cost_node

def dijkstras_algorithm():
    node = find_low_cost(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        
        processed.append(node)
        node = find_low_cost(costs)


dijkstras_algorithm()
print(costs)