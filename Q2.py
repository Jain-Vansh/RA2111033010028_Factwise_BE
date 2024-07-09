# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
 
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
 
# Your score is the sum of the points of the cards you have taken.
 
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

cardPoints = [1,2,3,4,5,6,1]
k = 3

ans = 0
l,r = 0,-1
temps = 0
for i in range (0,k):
    temps += cardPoints[i]
    ans = max(ans,temps)

temps = 0
for i in range(-1,-k-1,-1):
    temps += cardPoints[i]
    ans = max(ans,temps)

while(k > 0):
    if(cardPoints[l] != cardPoints[r]):
        temp = max(cardPoints[l],cardPoints[r])
        ans += max(temp,ans)
    k -= 1
print(ans)