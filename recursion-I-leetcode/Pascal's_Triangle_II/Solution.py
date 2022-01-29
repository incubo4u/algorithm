class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        results = {}
        rowIndex += 1

        def get(floor_nr, position):
            nonlocal results
            length = floor_nr - 1
            if floor_nr == 0 or position == 0 or position == length:
                return 1
            key = (length, position)
            if key in results:
                return results[key]
            results[key] = get(length, position - 1) + get(length, position)
            return results[key]
        floor = [0 for i in range(rowIndex)]
        for i in range(rowIndex):
            if i == 0 or i == rowIndex - 1:
                floor[i] = 1
            floor[i] = get(rowIndex, i)
        return floor
