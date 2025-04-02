from collections import deque

# Create an empty deque
dq = deque()
# Create a deque with initial elements
dq = deque([1,2,3,4,5])
print(dq)  # Output: deque([1, 2, 3, 4, 5])


# add
dq.append(5)       # Add 5 to the right
dq.appendleft(1)  #add 1 to the left 
print(dq)

#pop
dq.pop()      # Removes 5
dq.popleft()  # Removes 1
print(dq)