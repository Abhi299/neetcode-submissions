import time
from heapq import heappush, heapify, heappop

class Twitter:

    def __init__(self):
        self.fmap = defaultdict(set)
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((time.time(), tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = list(self.tweets[userId].copy())

        for followeeId in self.fmap[userId]:
            for e in self.tweets[followeeId]:
                heappush(minheap, e)
                if len(minheap) > 10:
                    heappop(minheap)

        minheap.sort(reverse=True)

        return [tweetId for _, tweetId in minheap]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.fmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fmap[followerId].discard(followeeId)
