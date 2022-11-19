def FU6OHA44U(N):
    MACCUB = []
    for i in range(N):
        if (i==0): MACCUB.append(1)
        if (i==1): MACCUB.append(1)
        if (i>1): MACCUB.append(MACCUB[i-1] + MACCUB[i-2])
    return MACCUB

def COPTUPOBKA(MACCUB):
    for i in range(len(MACCUB)-1):
        for j in range(len(MACCUB)-1):
            if MACCUB[j] > MACCUB[j+1]:
                MACCUB[j], MACCUB[j+1] = MACCUB[j+1], MACCUB[j]
    return MACCUB

def KAJIbKyJI9TOP(_4UCJIO1, _4UCJIO2, OnEPAuU9):
    if (OnEPAuU9 == "+"): return (_4UCJIO1 + _4UCJIO2)
    if (OnEPAuU9 == "-"): return (_4UCJIO1 - _4UCJIO2)
    if (OnEPAuU9 == "*"): return (_4UCJIO1 * _4UCJIO2)
    if (OnEPAuU9 == "/"): return (_4UCJIO1 / _4UCJIO2)



