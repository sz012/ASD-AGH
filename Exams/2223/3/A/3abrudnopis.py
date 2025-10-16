import heapq

def dijkstra(graph, start):
  distances = [float('inf') for node in graph]
  distances[start] = 0

  queue = [(0, start, 0)]
  while queue:
    curDist, curNode, curHrsAwake = heapq.heappop(queue)
    if curDist > distances[curNode]:
      continue

    for neighbor, weight in graph[curNode]:
      distance = curDist + weight

      if distance + curHrsAwake > 16:
          distance += 8
          curHrsAwake = 0
      else:
          curHrsAwake += distance

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(queue, (distance, neighbor, curHrsAwake))
  return distances

'''
distance = curDist + weight
if distance + hrsawake > 16:
    distance += 8
    hrsawake = 0
else:
    hrsawake += distance
'''