import requests

from json import loads
from Mods import mods_dict
from PP import PPCalc
from Mods_mask import applyMods

import configparser

# CONFIG ------------------

cfg = configparser.ConfigParser()
cfg.read('config.ini')

# -------------------------

def PP_Calculator(combo: int, beatmap_id: int=None, mods: list='nomod', score_v: int=1, f_accs: list=[0.90, 0.95, 1], f_miss: list=[0, 0, 0]) -> list:

    url = 'https://osu.ppy.sh/api/get_beatmaps'
    params = {'k': cfg['OSUAPI']['KEY'],
	      'b': beatmap_id}

    if mods != 'nomod':
        appble_mods = []
        [((appble_mods.append(i)) if i in ['dt', 'ht', 'hr', 'ez'] else '') for i in mods]
        params['mods'] = 0
        
        for i in appble_mods:
            params['mods'] += mods_dict[i]
    
    Beatmap = loads(requests.get(url=url, params=params).text)[0]
    res = list()

    for i in range(len(f_accs)):
        if f_accs[i] == 1:
            combo = 'max'
        
        res.append(PPCalc(None, combo, score_v, Beatmap, mods, f_acc=f_accs[i], f_miss=f_miss[i]))

    return (*applyMods(Beatmap, mods=mods), round(float(Beatmap['difficultyrating']), 2)), [round(i) for i in res], [Beatmap['title'], Beatmap['version'], Beatmap['hit_length']]
