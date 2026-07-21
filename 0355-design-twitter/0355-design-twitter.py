class Twitter:

    def __init__(self):
        self.following = {}
        self.posting = {}
        self.order = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.order -= 1
        if userId not in self.posting: 
            self.posting[userId] = [(self.order, tweetId)]
        else: self.posting[userId].append((self.order, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        allTweet = []
        if userId in self.posting:
            for i in self.posting[userId]:
                allTweet.append(i)

        if userId in self.following:
            for i in self.following[userId]:
                if i in self.posting:
                    for j in self.posting[i]:
                        allTweet.append(j)

        feed, posts = [], 0
        heapq.heapify(allTweet)
        while allTweet and posts < 10:
            posts += 1
            recent = heapq.heappop(allTweet)        
            feed.append(recent[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {followeeId}
        else: self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return
        else: self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)