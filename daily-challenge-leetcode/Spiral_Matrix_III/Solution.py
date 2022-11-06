class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, y: int, x: int) -> List[List[int]]:
        ans = [(y, x)]
        step = 0
        total = (rows * cols) - 1
        while total:
            step += 1

            for _ in range(step):
                x += 1
                if 0 <= x < cols and 0 <= y < rows:
                    total -= 1
                    ans.append((y, x))
            for _ in range(step):
                y += 1
                if 0 <= x < cols and 0 <= y < rows:
                    total -= 1
                    ans.append((y, x))

            step += 1
            for _ in range(step):
                x -= 1
                if 0 <= x < cols and 0 <= y < rows:
                    total -= 1
                    ans.append((y, x))
            for _ in range(step):
                y -= 1
                if 0 <= x < cols and 0 <= y < rows:
                    total -= 1
                    ans.append((y, x))

        return ans
