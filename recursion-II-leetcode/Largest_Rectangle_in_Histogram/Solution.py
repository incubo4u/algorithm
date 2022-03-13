
class Solution(object):
    def largestRectangleArea(self, heights):
        heights += [0]
        tracking = []
        maxArea = 0
        for i in range(len(heights)):
            last = len(heights) + 1
            while len(tracking) > 0 and heights[i] < tracking[-1][0]:
                last = tracking[-1][1]
                maxArea = max(maxArea, (i-last)*tracking.pop()[0])
            if len(tracking) == 0 or heights[i] > tracking[-1][0]:
                tracking.append((heights[i], min(last, i)))
        return maxArea


class Solution(object):
    def largestRectangleArea(self, heights):
        heights += [0]
        tracking = []
        maxArea = 0

        def find(i):
            nonlocal maxArea
            if i == len(heights):
                return maxArea
            last = len(heights) + 1
            while len(tracking) > 0 and heights[i] < tracking[-1][0]:
                last = tracking[-1][1]
                maxArea = max(maxArea, (i-last)*tracking.pop()[0])
            if len(tracking) == 0 or heights[i] > tracking[-1][0]:
                tracking.append((heights[i], min(last, i)))
            return find(i+1)
        return find(0)
