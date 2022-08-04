from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(SortedList)
        self.findstyle = {}
        for i in range(len(foods)):
            food,style,rate = foods[i],cuisines[i],ratings[i]
            self.data[style].add((-rate,food))
            self.findstyle[food] = [style,rate]
        return

    def changeRating(self, food: str, newRating: int) -> None:
        style,prevrate = self.findstyle[food]
        self.data[style].discard((-prevrate,food))
        self.data[style].add((-newRating,food))
        self.findstyle[food][1] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.data[cuisine][0][1]

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)