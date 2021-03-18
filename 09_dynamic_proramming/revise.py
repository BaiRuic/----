states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_station = set()

def greedy_algorithms(states_needed):
    while states_needed:
        best_station = None
        best_station_cover = set()
        for station, state_coverd in stations.items():
            coverd = state_coverd & states_needed
            if len(coverd) > len(best_station_cover):
                best_station_cover = coverd
                best_station = station

        final_station.add(best_station)
        states_needed -= best_station_cover
    

greedy_algorithms(states_needed)
print(final_station)
