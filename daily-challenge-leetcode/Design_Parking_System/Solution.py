class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        __slots__ = "mapping"
        self.mapping = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.mapping[carType] -= 1
        return self.mapping[carType] >= 0
