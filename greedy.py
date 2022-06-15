stations = {
    "kone": {'id', 'nv', 'ut'},
    'ktwo': {'wa', 'id', 'mt'},
    'kthree': {'or', 'nv', 'ca'},
    'kfour': {'nv', 'ut'},
    'kfive': {'ca', 'az'}
}
states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

final_stations = set()


def greedy_search(states_needed):

    while states_needed:
        states_covered = {}

        for station, states in stations.items():
            covered = states & states_needed
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = states
                states_needed -= states_covered
                final_stations.add(best_station)

    return final_stations

print(greedy_search(states_needed))