"""
Num: #1353. Maximum Number of Events That Can Be Attended
Link: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
Problem: 
    You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
    You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
    Return the maximum number of events you can attend.
Example 1:
    Input: events = [[1,2],[2,3],[3,4]]
    Output: 3
    Explanation: You can attend all the three events.
    One way to attend them all is as shown.
    Attend the first event on day 1.
    Attend the second event on day 2.
    Attend the third event on day 3.
Example 2:
    Input: events= [[1,2],[2,3],[3,4],[1,2]]
    Output: 4
Constraints:
    1 <= events.length <= 105
    events[i].length == 2
    1 <= startDayi <= endDayi <= 105
"""
"""
Key point
1. Sort the events based on starting day of the event
2. Now once you have this sorted events, every day check what are the events that can start today
3. for all the events that can be started today, keep their ending time in heap.
    - why we only need ending times ?
        i) from today onwards, we already know this event started in the past and all we need to know is when this event will finish
        ii) Also, another key to this algorithm is being greedy, meaning I want to pick the event which is going to end the soonest.
    - So how do we find the event which is going to end the soonest?
        i) brute force way would be to look at all the event's ending time and find the minimum, this is probably ok for 1 day but as we can only attend 1 event a day,
            we will end up repeating this for every day and that's why we can utilize heap(min heap to be precise) to solve the problem of finding the event with earliest ending time
4. There is one more cleaning step, the event whose ending time is in the past, we no longer can attend those event
5. Last but very important step, Let's attend the event if any event to attend in the heap.        
"""

# reverse sort과정      
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events) # number of events
        h = []          # min-heap (contains all the events we can attend)
        count = 0       # maximum number of events that can be attended
        
        events.sort(reverse = True)
        day = events[-1][0]
        
        while True:
            # Discard past events that cannot be attended
            while h and h[0] < day:
                heapq.heappop(h)
                
            # Add all events to the heap that start today
            while events and events[-1][0] == day:
                heapq.heappush(h, events.pop()[1])
            
            # Attend an event if possible
            if h:
                heapq.heappop(h)
                count += 1
                
            if len(events) == 0 and len(h) == 0:
                break
                
            day += 1
        return count

    
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events) # number of events
        h = []          # min-heap (contains all the events we can attend)
        count = 0       # maximum number of events that can be attended

        events.sort()
        i = 0;
        day = events[0][0]
        
        while True:
            # Discard past events that cannot be attended
            while h and h[0] < day:
                heapq.heappop(h)
                
            # Add all events to the heap that start today
            while i < n and events[i][0] == day:
                heapq.heappush(h, events[i][1])
                i += 1
            
            # Attend an event if possible
            if h:
                heapq.heappop(h)
                count += 1
                
            if i >= n and len(h) == 0:
                break
                
            day += 1
        
        return count

# Using for-loop
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events) # number of events
        h = []          # min-heap (contains all the events we can attend)
        count = 0       # maximum number of events that can be attended
        max_date = max(e for s, e in events)

        events.sort()
        i = 0;
        
        for day in range(events[0][0], max_date+1):
            # Discard past events that cannot be attended
            while h and h[0] < day:
                heapq.heappop(h)
                
            # Add all events to the heap that start today
            while i < n and events[i][0] == day:
                heapq.heappush(h, events[i][1])
                i += 1
            
            # Attend an event if possible
            if h:
                heapq.heappop(h)
                count += 1
                
            if i >= n and len(h) == 0:
                break
        
        return count