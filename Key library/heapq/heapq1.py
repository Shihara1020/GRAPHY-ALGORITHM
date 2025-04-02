import heapq

heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # Min heap: [1, 1, 3, 4, 5]

print(heapq)

#insert the value
heapq.heappush(heap, 2)  # Insert 2

print(heapq.heappop(heap))  # Removes 1 (smallest element)
