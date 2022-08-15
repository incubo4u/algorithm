class Solution:
    def cleanRoom(self, robot):
        directions = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
        cleaned = set()

        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def cleanAll(x=0, y=0, angle=0):
            robot.clean()
            cleaned.add((x, y))
            for i in range(4):
                nextAngle = (angle + i) % 4
                nextPos = (x + directions[nextAngle][0], y + directions[nextAngle][1])
                if nextPos not in cleaned and robot.move():
                    cleanAll(nextPos[0], nextPos[1], nextAngle)
                    goBack()
                robot.turnRight()

        cleanAll()
