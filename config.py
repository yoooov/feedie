# -*- coding: utf-8 -*-

feedie = {
    'bot_owner': ['meigrafd'],
    'cmd_prefix': '!',
    #'shorten_service': 'v.gd', #requires ssl
    'shorten_service': 'tinyurl.com',
}

network = {
    'server': 'irc.jen.de.euirc.net',
    'port': 6667,
    'password': '',
    'bot_nick': 'FEED',
    'bot_name': 'feedie pyBot v1.0',
    'pubmsg_log': False,
    'announce_delay': .5,
    'default_refresh_delay': 35.0,
    'startup_announces': False,
}

feeds = [{
    'mydealz': {
        'url': 'https://www.mydealz.de/rss/alle',
        'color': 'green',
        'channel': '#FEEDs',
        'channel_key': '',
        'enabled': True,
    },
    'monsterdealz': {
        'url': 'http://feeds.feedburner.com/MonsterDealz?format=xml',
        'color': 'green',
        'channel': '#FEEDs',
        'channel_key': '',
        'enabled': True,
    },
}]


# EOF
