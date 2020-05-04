import PP_Calculator
from pppredict.predict import predict

from util import str_to_dict, mod_convert
from json import loads
from re import findall

ERR_NP_NEED: str = 'You need to use /np before this command'

''' +====-----------==--------=----------- ------------   ------- -- ---   -
|
| PP Calculation
|
| Use /np before command*
|
| Syntax: {prefix}pp mods='nomod' acc=[95, 100] miss=[0, 0] combo='max'
| 
| If force_miss num are not equals to force_acc,
| for every force_acc with index > len(force_miss) will use force_miss[-1]
|
| *NOTE: kwargs must to be after args
|
| Returns message to send in format: For {title} [{dif_name}] ({OD}, {AR}, {CS}, {Stars}, {Len_in_minutes}) you'll get *[{i[PP]} for {i[ACC]}]
|
\==---=--------------------------- -------  ----   -   -'''


def calc(*args) -> str:
    try:
        Action: str = args[1][0][args[2]]

    except:
        return ERR_NP_NEED

    PPs: str = ''
    nick: str = args[-1]
    args: list = args[0]
    beatmap_ID: str = findall(r'\d+', Action[Action.find('/b/')+3:])[0]

    # If +MOD_NAME in Action, collect them to mods parameter
    if '+' in Action:
        mods = mod_convert(Action)
    else:
        mods = 'nomod'

    # if there are args
    if args:
        acc = [0.95, 1]
        miss = [0, 0]
        combo = 'max'
        arg_list = {'mods': [],
                    'acc': acc,
                    'miss': miss,
                    'combo': combo}

        # if there are keyword args
        if any('=' in i for i in args):
            kwargs: list = list()

            for i in range(len(args)):
                [(kwargs.append(i), args.remove(i)) if '=' in i else '' for i in args]

            for i in kwargs:
                if 'mods=' in i:
                    ind =  kwargs.index(i)
                    kwargs[ind] =  kwargs[ind][:5] + '"' + kwargs[ind][5:] + '"'

            # bruh
            kwargs = eval('str_to_dict({})'.format(', '.join(kwargs)))

            # some ifs, maybe better solution soon
            if 'mods' in kwargs:
                arg_list['mods'] = [i.lower() for i in [kwargs['mods'][i:i+2] for i in range(0, len(kwargs['mods']), 2)]]

            if 'acc' in kwargs:
                arg_list['acc'].insert(0, kwargs['acc']/100)

            if 'miss' in kwargs:
                arg_list['miss'].insert(0, kwargs['miss'])

            if 'combo' in kwargs:
                arg_list['combo'] = kwargs['combo']

        # if there are non-keyword args
        if args:
            # all non-keyword args type is str. For acc and miss it should be int
            for i in range(len(args)):
                if type(arg_list[list(arg_list.keys())[i]])  == 'str':
                    arg_list[list(arg_list.keys())[i]] = args[i]
                elif list(arg_list.keys())[i] == 'mods':
                    arg_list[list(arg_list.keys())[i]] = [x.lower() for x in [args[i][x:x+2] for x in range(0, len(args[i]), 2)]]
                elif list(arg_list.keys())[i] == 'acc':
                    arg_list[list(arg_list.keys())[i]].insert(0, float(args[i])/100)
                else:
                    arg_list[list(arg_list.keys())[i]].insert(0, int(args[i]))

        # If user sets acc but not misses or vise versa we should equalize arrays
        if len(arg_list['acc']) != len(arg_list['miss']):

            dif =  abs(len(arg_list['acc']) - len(arg_list['miss']))

            if len(arg_list['acc']) > len(arg_list['miss']):

                for i in range(dif):
                    arg_list['miss'].append(arg_list['miss'][-1])
            else:
                for i in range(dif):
                    arg_list['acc'].append(arg_list['acc'][-1])

        if arg_list['mods'] is False:
            arg_list['mods'] = mods

    else:
        arg_list = {
            'mods': mods,
            'acc': [0.95, 1],
            'miss': [0, 0],
            'combo': 'max'
            }

    res: list = PP_Calculator.PP_Calculator(arg_list['combo'],
                                               beatmap_ID,
                                               arg_list ['mods'],
                                               1,
                                               arg_list['acc'],
                                               arg_list['miss'])

    for i in range(len(res[1])):
        PPs += '| {}pp for {}% '.format(res[1][i], arg_list['acc'][i]*100)

    message = "For [https://osu.ppy.sh/b/{} {} [{}]{}] (OD {}, AR {}, CS {}, {}*, {}:{}) you'll get {} {}".format(
                                                                beatmap_ID, #Beatmap ID
                                                                res[2][0], #Title
                                                                res[2][1], #Diff_name
                                                                ' +{}'.format(''.join(arg_list['mods']).upper()) if arg_list['mods'] != 'nomod' else '', # If mods used
                                                                *[round(i, 2) for i in res[0]], #AR and etc
                                                                *[int(i) for i in divmod(int(res[2][2]), 60)], #True Seconds
                                                                PPs, #PPs
                                                                '({}x)'.format(arg_list['combo']) if arg_list['combo'] != 'max' else '') #If combo param used

    return message

#Actually a copy of calc function but with prediction.
def calcPred(*args) -> str:
    try:
        Action: str = args[1][0][args[2]]

    except:
        return ERR_NP_NEED

    PPs: str = ''
    nick: str = args[-1]
    args: list = args[0]
    beatmap_ID: str = findall(r'\d+', Action[Action.find('/b/')+3:])[0]

    # If +MOD_NAME in Action, collect them to mods parameter
    if '+' in Action:
        mods = mod_convert(Action)
    else:
        mods = 'nomod'

    # if there are args
    if args:
        acc = [0.95, 1]
        miss = [0, 0]
        combo = 'max'
        arg_list = {'mods': [],
                    'acc': acc,
                    'miss': miss,
                    'combo': combo}

        # if there are keyword args
        if any('=' in i for i in args):
            kwargs: list = list()

            for i in range(len(args)):
                [(kwargs.append(i), args.remove(i)) if '=' in i else '' for i in args]

            for i in kwargs:
                if 'mods=' in i:
                    ind =  kwargs.index(i)
                    kwargs[ind] =  kwargs[ind][:5] + '"' + kwargs[ind][5:] + '"'

            # bruh
            kwargs = eval('str_to_dict({})'.format(', '.join(kwargs)))

            # some ifs, maybe better solution soon
            if 'mods' in kwargs:
                arg_list['mods'] = [i.lower() for i in [kwargs['mods'][i:i+2] for i in range(0, len(kwargs['mods']), 2)]]

            if 'acc' in kwargs:
                arg_list['acc'].insert(0, kwargs['acc']/100)

            if 'miss' in kwargs:
                arg_list['miss'].insert(0, kwargs['miss'])

            if 'combo' in kwargs:
                arg_list['combo'] = kwargs['combo']

        # if there are non-keyword args
        if args:
            # all non-keyword args type is str. For acc and miss it should be int
            for i in range(len(args)):
                if type(arg_list[list(arg_list.keys())[i]])  == 'str':
                    arg_list[list(arg_list.keys())[i]] = args[i]
                elif list(arg_list.keys())[i] == 'mods':
                    arg_list[list(arg_list.keys())[i]] = [x.lower() for x in [args[i][x:x+2] for x in range(0, len(args[i]), 2)]]
                elif list(arg_list.keys())[i] == 'acc':
                    arg_list[list(arg_list.keys())[i]].insert(0, float(args[i])/100)
                else:
                    arg_list[list(arg_list.keys())[i]].insert(0, int(args[i]))

        # If user sets acc but not misses or vise versa we should equalize arrays
        if len(arg_list['acc']) != len(arg_list['miss']):

            dif =  abs(len(arg_list['acc']) - len(arg_list['miss']))

            if len(arg_list['acc']) > len(arg_list['miss']):

                for i in range(dif):
                    arg_list['miss'].append(arg_list['miss'][-1])
            else:
                for i in range(dif):
                    arg_list['acc'].append(arg_list['acc'][-1])

        if arg_list['mods'] is False:
            arg_list['mods'] = mods

    else:
        arg_list = {
            'mods': mods,
            'acc': [0.95, 1],
            'miss': [0, 0],
            'combo': 'max'
            }

    res: list = PP_Calculator.PP_Calculator(arg_list['combo'],
                                               beatmap_ID,
                                               arg_list ['mods'],
                                               1,
                                               arg_list['acc'],
                                               arg_list['miss'])

    for i in range(len(res[1])):
        PPs += '| {}pp for {}% '.format(res[1][i], arg_list['acc'][i]*100)

    Pred: predict.Prediction = predict.Prediction()
    Pred.predict(nick, float(res[0][3]))

    if Pred.predicted == 'Impossible':
        PP_Pred = 'Impossible to FC for you :('
    else:
        PP_Pred: float = "Future you {}pp".format(PP_Calculator.PP_Calculator('max',
                                              beatmap_ID,
                                              arg_list['mods'],
                                              1,
                                              (Pred.predicted * 0.01, ),
                                              (0, ))[1][0])


    message = "For [https://osu.ppy.sh/b/{} {} [{}]{}] (OD {}, AR {}, CS {}, {}*, {}:{}) you'll get {} {} # {}".format(
                                                                beatmap_ID, #Beatmap ID
                                                                res[2][0], #Title
                                                                res[2][1], #Diff_name
                                                                ' +{}'.format(''.join(arg_list['mods']).upper()) if arg_list['mods'] != 'nomod' else '', # If mods used
                                                                *[round(i, 2) for i in res[0]], #AR and etc
                                                                *[int(i) for i in divmod(int(res[2][2]), 60)], #True Seconds
                                                                PPs, #PPs
                                                                '({}x)'.format(arg_list['combo']) if arg_list['combo'] != 'max' else '', #If combo param used
                                                                PP_Pred) # Predicted pp
    return message

# INFO
def info(*args):
    mess = 'You can check commands info [https://pastebin.com/ZEBPuxix here]. [https://suroryz.github.io/surbot_osu/ Source & contact]'

    return mess

# List of commands and functions
cmd_list = {'pp': (calc, True),
            'pp_pred': (calcPred, True),
            'info': (info, False)}
