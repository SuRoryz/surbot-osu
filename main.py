import sys

sys.path.append('./bot/')
sys.path.append('./pp/')

import bancho

if __name__ == '__main__':

    print('SBOT v0.2')
    print('Before running bot connect to channles by using bot.connect(channel_name)\n',
          '*WITHOUT #')
    print('To run bot use bot.run()')

    bot = bancho.Sur()
    bot.login()
    
