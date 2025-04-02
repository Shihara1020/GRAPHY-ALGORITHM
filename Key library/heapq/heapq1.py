import heapq

heap = [3, 1, 4, 1, 5]
heapq.heapify(heap)  # Min heap: [1, 1, 3, 4, 5]

#insert the value
heapq.heappush(heap, 2)  # Insert 2


#Removes and returns the smallest element (O(log n))
print(heapq.heappop(heap))  # Removes 1 (smallest element)
