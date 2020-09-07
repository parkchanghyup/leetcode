import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # 그래프로 인접리스트 구현

        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))


        # 큐 생성
        Q= [(0,K)]
        dist = collections.defaultdict(int)
        #우선 순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입

        while Q:
            time, node = heapq.heappop(Q)
            if node not in list(dist):
                dist[node] = time
                for v,w in graph[node]:
                    heapq.heappush(Q,(w+time,v))
        if len(list(dist)) <N:
            return -1

        return max(list(dist.values()))
