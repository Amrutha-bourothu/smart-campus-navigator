import heapq


# Campus Graph
campus = {
    "Main Gate": {
        "CSE Block": 100,
        "ECE Block": 120
    },

    "CSE Block": {
        "Main Gate": 100,
        "Library": 80,
        "IT Block": 90,
        "Lab": 60
    },

    "Library": {
        "CSE Block": 80,
        "Canteen": 70
    },

    "Canteen": {
        "Library": 70,
        "Play Ground": 100
    },

    "Lab": {
        "CSE Block": 60,
        "IT Block": 50
    },

    "IT Block": {
        "CSE Block": 90,
        "Lab": 50,
        "Civil Block": 80
    },

    "ECE Block": {
        "Main Gate": 120,
        "Mech Block": 100
    },

    "Civil Block": {
        "IT Block": 80,
        "Mech Block": 90
    },

    "Mech Block": {
        "ECE Block": 100,
        "Civil Block": 90,
        "Play Ground": 80
    },

    "Play Ground": {
        "Canteen": 100,
        "Mech Block": 80
    }
}


# Dijkstra's Algorithm
def shortest_path(start, end):

    distances = {location: float("inf") for location in campus}
    previous = {location: None for location in campus}

    distances[start] = 0

    queue = [(0, start)]

    while queue:

        current_distance, current = heapq.heappop(queue)

        if current == end:
            break

        for neighbor, distance in campus[current].items():

            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current

                heapq.heappush(
                    queue,
                    (new_distance, neighbor)
                )

    # Create path
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return path, distances[end]


# Test
start = "Main Gate"
end = "Library"

path, distance = shortest_path(start, end)

print("Shortest Path:")
print(" -> ".join(path))

print("Distance:", distance, "meters")