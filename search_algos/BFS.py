def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:

        if neighbor in [target_value]:
          path.append(neighbor)
          return path
  
        else:
          temp = [neighbor, path+[neighbor]]
          bfs_queue.append(temp)