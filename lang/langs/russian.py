# Language samples file

class Samples:
    def __init__(self):
        #COMMANDS
        self.PP = """За [https://osu.ppy.sh/b/{} {} [{}]{}] (OD {}, AR {}, 
                        CS {}, {}*, {}:{}) вы получите {} {}"""

        self.PP_FOR = """| {}pp за {}% """

        self.PP_PRED = """За [https://osu.ppy.sh/b/{} {} [{}]{}] (OD {}, AR {}, 
                        CS {}, {}*, {}:{}) вы получите {} {} # {}"""

        self.PP_PRED_IMPOSSIBLE = """Увы, но вы пока не в состоянии ФК'шнуть это :<"""

        self.PP_PRED_FUTURE = """Вы должны получить: {}pp"""

        self.INFO = """Исходный код и информация о командах может быть найдена 
                    [https://suroryz.github.io/surbot-osu/ тут]"""

        self.LANG_CHANGED = """Язык успешно изменен. Переводчик: SuRory"""

        #ERRORS
        self.ERROR_SYNTAX = """"Вы ввели что-то неправильно. Посмотрите страницу помощи -> .info"""

        self.ERROR_NP_NEED = """Перед использованием команды, напишите /np"""

        self.ERROR_NO_LANGUAGE = """"Извините, но я не могу найти ваш язык в моей базе. 
                                    Попробуйте использовать код языка ISO 639-1. 
                                    Если ваш язык просто не поддерживается, вы можете помочь переводом
                                    [https://suroryz.github.io/surbot-osu/lang/langs тут]"""

