#### Reference:
    English: https://docs.python.org/3/library/heapq.html
    Korean: https://docs.python.org/ko/3/library/heapq.html

#### When we use heap?: Usually, if you need to ask the minimum and maximum values frequently, use the heap!

#### Good Problems I think in LeetCode : 253, 378, 1353, 1642

#### Function
1. heapq.heappush(heap, item)
Push the value item onto the heap, maintaining the heap invariant.

2. heapq.heappop(heap)
Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].

3. heapq.heappushpop(heap, item)
Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

4. heapq.heapify(x)
Transform list x into a heap, in-place, in linear time.


#### Application
1. How to import module 'heapq'
: heapq module is one of built-in modules. So, you can simply import module using below code.

```python
import heapq
```

2. How to build min-heap
In python, list type is implemented as min-heap. Therefore, you should create a list at first.

3. How to add elements into heap
Using "heappush()" 

```python
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
```
```python
[1, 3, 7, 4]
```

4. How to remove an elements in heap
```python
print(heapq.heappop(heap))
print(heap)
```
```python
1
[3, 4, 7]
```

5. How to get a minmum element without deleting it
Simply, use list's characteristic.

```python
print(heap[0])
```
```python
3
```

6. How to change list to heap
Use 'heapify()'

```python
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)
```
```python
[1, 3, 5, 4, 8, 7]
```

7. max-heap
Since the heapq module only operates on the min-heap, some tricks are needed to utilize it as the max-heap.
When a tuple is added or deleted as an element in the heap, it uses the principle that the min-heap is constructed based on the first value in the tuple.

So, to create a max heap, you can find the priority of each value, and then add or delete a tuple of the (priority, value) structure from the heap. And when reading an element from the heap, just take the element at index 1 from each tuple. (since we want to know only the value, not priority)

```python
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (priority, value)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
```
```python
8
7
5
4
3
1
```

8. kth smallest/biggest value
```python
import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))
```
```python
4
```

9. Heap-sort
```python
import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
```
```python
[1, 3, 4, 5, 7, 8]
```
