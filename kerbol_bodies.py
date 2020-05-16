GM = 1.172 * (10 ** 18)

kerbol = {
    'moons': None,
    'low orbit': 610,
    'atmo': True,
    'mass': '1.7565459×10^28',
    'ap': 261600,
    'pe': 261600,
    'period': None
}

moho = {
    'moons': None,
    'low orbit': 50,
    'atmo': False,
    'mass': '2.5263314×10^21',
    'ap': 6315765.981,
    'pe': 4210510.628,
    'period': 2215754,
}

gilly = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.2420363×10^17',
    'ap': 48825.000,
    'pe': 14175.000,
    'period': 388587
}

eve = {
    'moons': [gilly],
    'low orbit': 100,
    'atmo': True,
    'mass': '1.2243980×10^23',
    'ap': 9931011.387,
    'pe': 9734357.701,
    'period': 5657995,
}

mün = {
    'moons': True,
    'low orbit': 14,
    'atmo': False,
    'mass': '9.7599066×10^20',
    'ap': 12000.000,
    'pe': 12000.000,
    'period': 138984,
}

minmus = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '2.6457580×10^19',
    'ap': 47000.000,
    'pe': 47000.000,
    'period': 1077311,
}

kerbin = {
    'moons': [mün, minmus],
    'low orbit': 80,
    'atmo': True,
    'mass': '5.2915158×10^22',
    'ap': 13599840.256,
    'pe': 13599840.256,
    'period': 9203545,
}

ike = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '2.7821615×10^20',
    'ap': 3296.000,
    'pe': 3104.000,
    'period': 65518,
}

duna = {
    'moons': [ike],
    'low orbit': 60,
    'atmo': True,
    'mass': '4.5154270×10^21',
    'ap': 21783189.163,
    'pe': 19669121.365,
    'period': 17315400,
}

dres = {
    'moons': None,
    'low orbit': 12,
    'atmo': False,
    'mass': '3.2190937×10^20',
    'ap': 46761053.692,
    'pe': 34917642.714,
    'period': 47893063,
}

laythe = {
    'moons': True,
    'low orbit': 60,
    'atmo': True,
    'mass': '2.9397311×10^22',
    'ap': 27184.000,
    'pe': 27184.000,
    'period': 52981,
}

vall = {
    'moons': True,
    'low orbit': 15,
    'atmo': False,
    'mass': '3.1087655×10^21',
    'ap': 43152.000,
    'pe': 43152.000,
    'period': 105962,
}

tylo = {
    'moons': True, 
    'low orbit': 10,
    'atmo': False,
    'mass': '4.2332127×10^22',
    'ap': 68500.000,
    'pe': 68500.000,
    'period': 211926,
}

bop = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '3.7261090×10^19',
    'ap': 158697.500,
    'pe': 98302.500,
    'period': 544507,
}

pol = {
    'moons': True,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.0813507×10^19',
    'ap': 210624.207,
    'pe': 149155.794,
    'period': 901903,
}

jool = {
    'moons': [laythe, vall, tylo, bop, pol],
    'low orbit': 210,
    'atmo': True,
    'mass': '4.2332127×10^24',
    'ap': 72212238.387,
    'pe': 65334882.253,
    'period': 104661432,
}

eeloo = {
    'moons': None,
    'low orbit': 10,
    'atmo': False,
    'mass': '1.1149224×10^21',
    'ap': 113549713.200,
    'pe': 66687926.800,
    'period': 156992048,
}

bodies = [kerbol, moho, eve, kerbin, duna, dres, jool, eeloo]