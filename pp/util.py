import requests
from Mods import mods_dict

def black_magic(nobjs, acc, misses):
    n100 = round(-3.0 * ((acc - 1.0) * nobjs + misses) * 0.5)

    return n100

def str_to_dict(**kwargs) -> dict:
    return kwargs

def getBeatmap(key, id_, mods='nomod'):
    url = 'https://osu.ppy.sh/api/get_beatmaps'
    params = {'k': key,
	      'b': id_}

    if mods != 'nomod':
        appble_mods = []
        [((appble_mods.append(i)) if i in ['dt', 'ht', 'hr', 'ez'] else '') for i in mods]
        params['mods'] = 0

        for i in appble_mods:
            params['mods'] += mods_dict[i]

    return requests.get(url, params).text

def mod_convert(mods: str):
    mod_list = {
        'hardrock': 'hr',
        'doubletime': 'dt',
        'hidden': 'hd',
        'easy': 'ez',
        'flashlight': 'fl',
        'halftime': 'ht'
        }

    res = list()
    mods = mods[mods.index('+')+1:].strip('+').split()
    for i in mods:
        try:
            res.append(mod_list[i.lower()])
        except:
            continue

    return res
