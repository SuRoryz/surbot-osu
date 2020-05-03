import sys

import configparser
import requests
import asyncio
from json import loads
from util import getBeatmap


# CONFIG ---------------------

cfg = configparser.ConfigParser()
cfg.read('config.ini')

#------------------------------

# User class
class User:
    def __init__(self) -> None:
        self.KEY: str = cfg['OSUAPI']['KEY']
        self.API_STAT: str = 'https://osu.ppy.sh/api/get_user'
        self.API_SCORES: str = 'https://osu.ppy.sh/api/get_user_best'

        self.name: str = ''
        self.data: dict = dict()
        self.acc: float = 100.0
        #Will be used soon
        self.pp: float = 0.0

        self.scores: dict = dict()
        self.avg_score_pp: float = 0.0
        self.star_avg: float = 0.0

    def start(self, name: str) -> None:
        #Get info about player
        self.setUser(name)
        #Calculate avg stars from user's top 10 scores
        self.calcAvgStar()

    def setUser(self, name: str) -> None:
        self.name = name
        PARAMS_DATA: dict = {'k': self.KEY, 'u': self.name}
        PARAMS_SCORES: dict = {'k': self.KEY, 'u': self.name, 'limit': 10}

        self.scores = loads(requests.get(self.API_SCORES, PARAMS_SCORES).text)
        self.data = loads(requests.get(self.API_STAT, PARAMS_DATA).text)[0]

        self.acc = float(self.data['accuracy'])
        self.pp = float(self.data['pp_raw'])

    def calcAvgStar(self) -> None:
        bm_stars: list = list()
        for score in self.scores:
            bm_stars.append(float(loads(getBeatmap(self.KEY, score['beatmap_id']))[0]['difficultyrating']))
            self.star_avg = sum(bm_stars)/10