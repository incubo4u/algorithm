from bisect import bisect_right


class SnapshotArray:

    def __init__(self, length: int):
        self.id = 0
        self.d = [[(0, 0)] for _ in range(length)]

    def set(self, i: int, val: int) -> None:
        self.d[i].append((val, self.id))

    def snap(self) -> int:
        self.id += 1
        return self.id - 1

    def get(self, i: int, snap_id: int) -> int:
        j = min(bisect_right(self.d[i], snap_id, key=lambda t: t[1]),
                len(self.d[i]) - 1)
        if self.d[i][j][1] > snap_id:
            j -= 1
        return self.d[i][j][0]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
