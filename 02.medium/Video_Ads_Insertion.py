#https://datalemur.com/questions/python-video-ads-insertion

#you can't place a video ad next to an existing video
# can't place a video ad next to a non-video ad

#0 denotes a normal post
#1 denotes a video
#2 denotes a non-video ad

feed_items = [1, 2, 0, 0, 0]

n = 3

def can_insert_ads(feed_items, n):
    new_ads = 0
    consecutive_z = 0
    
    if feed_items[0] == 0:
      new_ads += 1
    
    for i in range(len(feed_items)):
      if feed_items[i] != 0:
        if consecutive_z > 1:
          new_ads += (consecutive_z - 1)
        if new_ads >= n:
          return True
        consecutive_z = 0
      else:
        consecutive_z += 1
        
    if feed_items[-1] == 0:
      new_ads += 1
      
    if consecutive_z > 1:
      new_ads += (consecutive_z-1)
    
    if new_ads >= n:
      return True
    else:
      return False


