#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#

# @lc code=start
class Twitter(object):

    def __init__(self):
        self.users = {} # recording the current userID(int) and follower list
        self.posts = [] # Recording the userID, tweetID

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.posts.append([userId, tweetId]) # add post into the posts list
        if not self.users.get(userId): # update the users list
            self.users[userId] = []
        
    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        if userId not in self.users.keys():
            return 
        else:
            ids = [userId] + self.users.get(userId) # getting the id and its followers
            tmpresult = []
            count = 10
            for post in self.posts[-1: -(len(self.posts) + 1):-1]: # check in a reverse order
                if count > 0:
                    if post[0] in ids: # if userid and its followers has post news  
                        tmpresult.append(post[1])
                        count -= 1
            return tmpresult

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users.keys():
            self.users.setdefault(followerId, []).append(followeeId)
        else:
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.users.keys():
            return
        else:
            if followeeId in self.users[followerId]:  # check its legality and remove it
                self.users[followerId].remove(followeeId)
            else:
                return




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

