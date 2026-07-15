import time

class Twitter:

    def __init__(self):
        # {
        #     userId1: {
        #         followers: [userId2,userId3],
        #         followees: [userId2,userId3,userId4],
        #         tweets: [tweetId1]
        #     }
        # } 
        self.userTweets = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userTweets:
            self.userTweets[userId]={
                # 'followers': [],
                'followees': [userId],
                'tweets': []
            }
        self.userTweets[userId]['tweets'].append({'tweetId':tweetId, 'createdAt':time.time()})
        # for userId in self.userTweets[userId][followees]:

        print(self.userTweets)
        return        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets=[]
        for followeeId in self.userTweets[userId]['followees']:
            tweets+=self.userTweets[followeeId]['tweets']
        
        tweets.sort(key = lambda x:x['createdAt'], reverse=True)
        tweetIds = map(lambda x:x['tweetId'], tweets)
        return (list(tweetIds))[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.userTweets:
            self.userTweets[followerId]={
                'followees': [followerId],
                'tweets': []
            }
        if followeeId not in self.userTweets[followerId]['followees']:
            self.userTweets[followerId]['followees'].append(followeeId)
        return        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.userTweets:
            self.userTweets[followerId]={
                'followees': [followerId],
                'tweets': []
            }
        if followeeId in self.userTweets[followerId]['followees']:
            self.userTweets[followerId]['followees'].remove(followeeId)
        return
