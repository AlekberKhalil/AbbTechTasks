class Solution:
    def carParkingRoof(self, cars, k):
      n=4
      cars=[6, 2, 12, 7]
      k=3        
        cars.sort()
        n = len(cars)
        res = float('inf')
        for i in range(n-k+1):
            res = min(res, cars[i+k-1] - cars[i])
        return res+1
