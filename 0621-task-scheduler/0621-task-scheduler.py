class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0: return len(tasks)
        cnt = Counter(tasks)

        h = [-i for i in cnt.values()]
        heapq.heapify(h)

        q = deque()
        time = 0

        while h or q:
            time += 1
            if h:
                most = heapq.heappop(h)
                most += 1
                if most != 0: q.append((most, time + n))

            if q and q[0][1] == time:
                left = q.popleft()
                heapq.heappush(h, left[0])

        return time