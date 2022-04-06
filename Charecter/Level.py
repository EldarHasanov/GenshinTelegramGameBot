class Level:
    experienceCost = (0, 1000, 1325, 1700, 2150, 2625, 3150, 3725, 4350, 5000, 5700, 6450,
                      7225, 8050, 8925, 9825, 10750, 11725, 12725, 13775, 14875, 16800, 18000,
                      19250, 20550, 21875, 23250, 24650, 26100, 27575, 29100, 30650, 32250, 33875,
                      35550, 37250, 38975, 40750, 42575, 44425, 46300, 50625, 52700, 54775, 56900,
                      59075, 61275, 63525, 65800, 68125, 70475, 76500, 79050, 81650, 84275, 86950,
                      89650, 92400, 95175, 98000, 100875, 108950, 112050, 115175, 118325, 121525,
                      124775, 128075, 131400, 134775, 138175, 148700, 152375, 156075, 159825, 163600,
                      167425, 171300, 175225, 179175, 183175, 216225, 243025, 273100, 306800, 344600,
                      386950, 434425, 487625, 547200)
    phaseUpGrade = (0, 20, 40, 50, 60, 70, 80, 90)

    def __init__(self, lvl=1):
        self.lvl = lvl
        self.experiencePoints = 0
        self.phaseUp = 1

    def __get__(self, instance, owner):
        return self.lvl

    def __set__(self, instance, value):
        lvl = self.levels_up(value)

    def levels_up(self, points):
        levelsUps = 0
        while self.experienceCost[self.lvl + levelsUps] < points:
            if levelsUps + self.lvl == self.phaseUpGrade[self.phaseUp]:
                self.experiencePoints = 0
                return levelsUps + self.lvl
            points -= self.experienceCost[self.lvl + levelsUps]
            levelsUps += 1
        self.experiencePoints = points
        return levelsUps + self.lvl

    def phases_up(self):
        if self.lvl == self.phaseUpGrade[self.phaseUp]:
            self.phaseUp += 1
            self.experiencePoints = 0
