from collections import deque

# Create an empty deque
dq = deque()
# Create a deque with initial elements
dq = deque([1,2,3,4,5])
dq.append(5)       # Add 5 to the right
dq.appendleft(1) 
print(dq)  # Output: deque([1, 2, 3, 4, 5])
