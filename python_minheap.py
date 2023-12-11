class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        combined = []
        for start,end, profit in zip(startTime, endTime, profit):
            combined.append([start, end, profit])
            
        combined.sort(key = lambda x:x[0])
        maxProfit = 0
        minheap = []
    
        
        for start, end, profit in combined:
            while minheap and minheap[0][0] <= start:
                e, p = heapq.heappop(minheap)
                maxProfit = max(maxProfit, p)

            heapq.heappush(minheap, [end, profit + maxProfit])
        
        while minheap:
            maxProfit = max(maxProfit, minheap[0][1])
            heapq.heappop(minheap)
            
        return maxProfit
