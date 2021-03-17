states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_station = set()

def greedy_algorithms(states_needed):
    while states_needed:   # 大循环 此时里面的都是当前待覆盖的， 然后一个循环找一个最佳电台 
        best_station = None
        states_covered = set()
        
        for station, cover_states in stations.items():
            covered = states_needed & cover_states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_station.add(best_station)


greedy_algorithms(states_needed)
print(final_station)