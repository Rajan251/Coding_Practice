import heapq

def beauty(n, m, S):
    graph = [[] for _ in range(26)] # adjacency list for each alphabet
    for i in range(m):
        u, v = input().split()
        graph[ord(u)-ord('a')].append(ord(v)-ord('a'))

    def dijkstra(start, end):
        max_beauty = -1
        visited = set()
        pq = [(-1, [start])] # priority queue of (-beauty, path) tuples
        while pq:
            beauty, path = heapq.heappop(pq)
            if -beauty < max_beauty:
                break
            node = path[-1]
            if node == end:
                return -beauty, path
            if node in visited:
                continue
            visited.add(node)
            freq = [0] * 26 # frequency of each alphabet along the path
            for p in path:
                freq[p] += 1
            for neighbor in graph[node]:
                heapq.heappush(pq, (-max(freq[neighbor], -beauty), path + [neighbor]))
            max_beauty = max(max_beauty, -beauty)
        return -1, []

    return dijkstra(ord(S[0])-ord('a'), ord(S[n-1])-ord('a'))[0]