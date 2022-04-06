import numpy as np


class ElementalSkill:
    def __init__(self, percentage):
        # base stats
        self.percentage = percentage

    def use_e(self):
        print("use e")

    def use_hold_e(self):
        print("use hold e")
