class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = [stationName,t]
        return

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        cinStation,cinTime = self.checkins[id]
        if cinStation + "-" + stationName in self.stations:
            self.stations[cinStation + "-" + stationName][0] += t - cinTime
            self.stations[cinStation + "-" + stationName][1] += 1
        else:
            self.stations[cinStation + "-" + stationName] = [t - cinTime,1]
        return

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time,persons = self.stations[startStation + "-" + endStation]
        return time / persons


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)