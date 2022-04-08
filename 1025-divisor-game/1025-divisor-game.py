class Solution:
    def divisorGame(self, n: int) -> bool:
        def gameHelper(n,state):
            if n < 2:
                if state == 0:
                    return False
                return True
            
            if state == 0:
                for i in range(1,n):
                    if n % i == 0:
                        return gameHelper(n-i,1)
            if state == 1:
                for i in range(1,n):
                    if n % i == 0:
                        return gameHelper(n-i,0)
            
        return gameHelper(n,0)