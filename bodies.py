kerbol = {
    'moons': None,
    'low orbit' = 610
    'atmo' = True
    'mass' = '1.7565459×10^28'
}

moho = {
    'moons': None,
    'low orbit' = 50
    'atmo' = False
    'mass' = '2.5263314×10^21'
}

gilly = {
    'moons': True,
    'low orbit' = 10
    'atmo' = False
    'mass' = '1.2420363×10^17' 
}

eve = {
    'moons': [gilly],
    'low orbit' = 100
    'atmo' = True
    'mass' = '1.2243980×10^23'
}

mün = {
    'moons': True,
    'low orbit' = 14
    'atmo' = False
    'mass' = '9.7599066×10^20'
}

minmus = {
    'moons': True,
    'low orbit' = 10
    'atmo' = False
    'mass' = '2.6457580×10^19'
}

kerbin = {
    'moons': [mün, minmus],
    'low orbit' = 80
    'atmo' = True
    'mass' = '5.2915158×10^22'
}

ike = {
    'moons': True,
    'low orbit' = 10
    'atmo' = False
    'mass' = '2.7821615×10^20'
}

duna = {
    'moons': [ike],
    'low orbit' = 60
    'atmo' = True
    'mass' = '4.5154270×10^21'
}

dres = {
    'moons': None,
    'low orbit' = 12
    'atmo' = False
    'mass' = '3.2190937×10^20'
}

laythe = {
    'moons': True,
    'low orbit' = 60
    'atmo' = True
    'mass' = '2.9397311×10^22'
}

vall = {
    'moons': True,
    'low orbit' = 15
    'atmo' = False
    'mass' = '3.1087655×10^21'
}

tylo = {
    'moons': True, 
    'low orbit' = 10
    'atmo' = False
    'mass' = '4.2332127×10^22'
}

bop = {
    'moons': True
    'low orbit' = 10
    'atmo' = False
    'mass' = '3.7261090×10^19'
}

pol = {
    'moons': True
    'low orbit' = 10
    'atmo' = False
    'mass' = '1.0813507×10^19'
}

jool = {
    'moons': [laythe, vall, tylo, bop, pol],
    'low orbit' = 210
    'atmo' = True
    'mass' = '4.2332127×10^24'
}

eeloo = {
    'moons': None
    'low orbit' = 10
    'atmo' = False
    'mass' = '1.1149224×10^21'
}

bodies = [kerbol, moho, eve, kerbin, duna, dres, jool, eeloo]