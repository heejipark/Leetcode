"""
Num: # 253. Meeting Rooms II
Link: https://leetcode.com/problems/meeting-rooms-ii/
Problem: 
    Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2
Example 2:
    Input: intervals = [[7,10],[2,4]]
    Output: 1
 Constraints:
    1 <= intervals.length <= 104
    0 <= start i < end i <= 106
"""

# key point- sorting, using min-heap
"""
    1. Sort the given meetings by their start time.
    2. Initialize a new min-heap and add the first meeting's ending time to the heap. 
       We simply need to keep track of the ending times as that tells us when a meeting room will get free
    3. For every meeting room check if the minimum element of the heap.
       i.e. the room at the top of the heap is free or not.
    4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
    5. If not, then we allocate a new room and add it to the heap.
    6. After processing all the meetings, the size of the heap will tell us the number of rooms allocated.
       This will be the minimum number of rooms needed to accomodate all the meetings.
"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # If there is no meeting to schedule then no room needs to be allocated
        if not intervals:
            return 0
        
        # The heap initialization
        free_rooms = []
        
        # Sort the meetings in increasing order of their start time
        intervals.sort(key=lambda x: x[0])
        
        # Add the first meeting, we have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0][1])
        
        # For all the remaining meeting rooms
        for curStart, curEnd in intervals[1:]:
            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= curStart: # if the start time is later than the end time of the first meeting room
                heapq.heappop(free_rooms)   # pop the first room and push the room
                
            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time
            heapq.heappush(free_rooms, curEnd)
            
        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)
                
"""
* Time complexity: O(NlogN)
    - There are two major portions that take up time here.
    1) One is sorting of the array that takes O(NlogN) considering that the array consists of N elements.
    2) Then we have the min-heap. In the worst case, all N meetings will collide with each other.
    In any case we have N add operations on the heap.
    In the worst case we will have N extract-min operations as well.
    Overall complexity being NlogN since extract-min operation on a heap takes O(logN)
* Space complexity: O(N)
    - O(N) because we construct the min-heap and that can contain N elements in the worst case as described above in the time complexity section.
    - Hence, the space complexity is O(N)

* Runtime: 134 ms, faster than 24.97% of Python3 online submissions for Meeting Rooms II.
* Memory Usage: 17.4 MB, less than 82.52% of Python3 online submissions for Meeting Rooms II.
"""      
                