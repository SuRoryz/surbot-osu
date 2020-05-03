import sys

import asyncio
from pppredict.userApi import user

#Prediction class
class Prediction:
    def __init__(self):
        self.name: str = ''
        self.stars: float = 0.0
        self.user: user.User = user.User()
        self.predicted: float = 100.0

    def predict(self, user: str, stars: float) -> None:
        self.name = user
        self.stars = stars

        #Getting info about player and his scores
        self.user.start(self.name)

        #Process prediction
        self.process()

    def process(self) -> None:
        #Set range around user's acc
        acc_range: float = self.user.acc * (1 - self.user.acc/100)
        max_ = min(100, self.user.acc + (acc_range*1.625))
        min_ = abs(self.user.acc - (acc_range*1.625))
        #Calc acc
        self.predicted = max(min_, min(max_, self.user.acc + (self.user.star_avg-self.stars) * (8*acc_range/self.user.star_avg)))
        if self.predicted == min_:
            self.predicted = "Impossible"