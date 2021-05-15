from heapq import heappop, heappush
import math
from math import inf
from manhattan_graph import manhattan_graph, penn_station, grand_central_station

graph = {
        'A': [('B', 10), ('C', 3)],
        'C': [('D', 2)],
        'D': [('E', 10)],
        'E': [],
        'B': [('C', 3), ('D', 2)]
    }


def dijkstras(graph, start):
  distances = {}
  for vertex in graph:
    distances[vertex] = inf
  distances[start] = 0
  vertices_to_explore = [(0, start)]

  while vertices_to_explore:
    current_distance,current_vertex  = heappop(vertices_to_explore)
    for neighbor,edge_weight in graph[current_vertex]:
      new_distance = current_distance+edge_weight
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance
        heappush(vertices_to_explore,(new_distance,neighbor))
  return distances
        
distances_from_a = dijkstras(graph, 'A')
print("\n\nShortest Distances: {0}".format(distances_from_a))


def manhattan(start, target):
    x_distance = abs(start.position[0] - target.position[0])
    y_distance = abs(start.position[1] - target.position[1])
    return x_distance + y_distance

# Euclidean Heuristic:
def euclidean(start, target):
    x_distance = abs(start.position[0] - target.position[0])**2
    y_distance = abs(start.position[1] - target.position[1])**2
    return math.sqrt(x_distance + y_distance )


def a_star(graph, start, target):
  print("Starting A* algorithm!")
  count = 0
  paths_and_distances = {}
  for vertex in graph:
    paths_and_distances[vertex] = [inf, [start.name]]
  
  paths_and_distances[start][0] = 0
  vertices_to_explore = [(0, start)]
  while vertices_to_explore and paths_and_distances[target][0] == inf:
    current_distance, current_vertex = heappop(vertices_to_explore)
    for neighbor, edge_weight in graph[current_vertex]:
      new_distance = current_distance + edge_weight + euclidean(neighbor,target)
      new_path = paths_and_distances[current_vertex][1] + [neighbor.name]
      
      if new_distance < paths_and_distances[neighbor][0]:
        paths_and_distances[neighbor][0] = new_distance
        paths_and_distances[neighbor][1] = new_path
        heappush(vertices_to_explore, (new_distance, neighbor))
        count += 1
        print("\nAt " + vertices_to_explore[0][1].name)
        
  print("Found a path from {0} to {1} in {2} steps: ".format(start.name, target.name, count), paths_and_distances[target][1])
  return paths_and_distances[target][1]

# Call a_star() on manhattan_graph to find the best route
# from penn_station to grand_central_station:
a_star(manhattan_graph, penn_station, grand_central_station)


