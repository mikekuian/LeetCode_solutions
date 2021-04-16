# A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

# Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

# In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:



class Solution:
   
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        eps = 10 ** -12
        def gradient(x, y):
            dx = 0
            dy = 0
            cost = 0
            for xi, yi in positions:
                l2 = sqrt((x - xi) ** 2 + (y - yi) ** 2)
                dx += (x - xi) / (l2 + eps) 
                dy += (y - yi) / (l2 + eps)
                cost += l2
            return dx, dy, cost

        def init():
            n = len(positions)
            return sum(x for x, _ in positions) / n, sum(y for _, y in positions) / n

        x, y = init()
        decay = 1 - (10 ** -3)
        stepSize = 10
        prev = 1
        cost = 0

        while abs(cost - prev) > 10 ** -16:
            prev = cost
            dx, dy, cost = gradient(x, y)
            
            deltaX = -dx * stepSize
            deltaY = -dy * stepSize
            x += deltaX
            y += deltaY
            stepSize *= decay
        
        return cost
