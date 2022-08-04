from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(dict)
        self.sortord = defaultdict(SortedList)
        self.prev = {}
        for i in range(len(foods)):
            food = foods[i]
            country = cuisines[i]
            rate = ratings[i]
            if rate not in self.data[country]:
                self.data[country][rate] = SortedList()
                self.sortord[country].add(rate)
            self.data[country][rate].add(food)
            self.prev[food] = [country,rate]
        return 

    def changeRating(self, food: str, newRating: int) -> None:
        country,prevrate = self.prev[food]
        self.data[country][prevrate].discard(food)
        if len(self.data[country][prevrate]) == 0:
            self.data[country].pop(prevrate)
            self.sortord[country].discard(prevrate)
        self.prev[food][1] = newRating
        
        if newRating not in self.data[country]:
            self.data[country][newRating] = SortedList()
            self.sortord[country].add(newRating)
        self.data[country][newRating].add(food)
        return

    def highestRated(self, cuisine: str) -> str:
        highval = self.sortord[cuisine][-1]
        return self.data[cuisine][highval][0]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)