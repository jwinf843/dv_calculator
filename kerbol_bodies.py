GM = 1.172 * (10 ** 18)

kerbol = {
    'moons': None,
    'low orbit': 610,
    'atmo': True,
    'mass': '1.7565459×10^28',
    'ap': 261600000,
    'pe': 261600000,
    'period': None
}

moho = {
    'moons': None,
    'low orbit': 50,
    'atmo': False,
    'mass': '2.5263314×10^21',
    'ap': 6315765981,
    'pe': 4210510628,
    'period': 2215754,
}

gilly = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.2420363×10^17',
    'period': 388587,
    'ap': 48825000,
    'pe': 14175000,
    'period': 388587
}

eve = {
    'moons': [gilly],
    'low orbit': 100,
    'atmo': True,
    'mass': '1.2243980×10^23',
    'ap': 9931011387,
    'pe': 9734357701,
    'period': 5657995,
}

mün = {
    'moons': True,
    'low orbit': 14,
    'atmo': False,
    'mass': '9.7599066×10^20',
    'ap': 12000000,
    'pe': 12000000,
    'period': 138984,
}

minmus = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '2.6457580×10^19',
    'ap': 47000000,
    'pe': 47000000,
    'period': 1077311,
}

kerbin = {
    'moons': [mün, minmus],
    'low orbit': 80,
    'atmo': True,
    'mass': '5.2915158×10^22',
    'ap': 13599840256,
    'pe': 13599840256,
    'period': 9203545,
}

ike = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '2.7821615×10^20',
    'ap': 3296000,
    'pe': 3104000,
    'period': 65518,
}

duna = {
    'moons': [ike],
    'low orbit': 60,
    'atmo': True,
    'mass': '4.5154270×10^21',
    'ap': 21783189163,
    'pe': 19669121365,
    'period': 17315400,
}

dres = {
    'moons': None,
    'low orbit': 12,
    'atmo': False,
    'mass': '3.2190937×10^20',
    'ap': 46761053692,
    'pe': 34917642714,
    'period': 47893063,
}

laythe = {
    'moons': True,
    'low orbit': 60,
    'atmo': True,
    'mass': '2.9397311×10^22',
    'ap': 27184000,
    'pe': 27184000,
    'period': 52981,
}

vall = {
    'moons': True,
    'low orbit': 15,
    'atmo': False,
    'mass': '3.1087655×10^21',
    'ap': 43152000,
    'pe': 43152000,
    'period': 105962,
}

tylo = {
    'moons': True, 
    'low orbit': 10,
    'atmo': False,
    'mass': '4.2332127×10^22',
    'ap': 68500000,
    'pe': 68500000,
    'period': 211926,
}

bop = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '3.7261090×10^19',
    'ap': 158697500,
    'pe': 98302500,
    'period': 544507,
}

pol = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.0813507×10^19',
    'ap': 210624207,
    'pe': 149155794,
    'period': 901903,
}

jool = {
    'moons': [laythe, vall, tylo, bop, pol],
    'low orbit': 210,
    'atmo': True,
    'mass': '4.2332127×10^24',
    'ap': 72212238387,
    'pe': 65334882253,
    'period': 104661432,
}

eeloo = {
    'moons': None,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.1149224×10^21',
    'ap': 113549713200,
    'pe': 66687926800,
    'period': 156992048,
}

bodies = [kerbol, moho, eve, kerbin, duna, dres, jool, eeloo]