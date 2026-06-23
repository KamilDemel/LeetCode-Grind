def snow(T,I):
    events = []
    for a,b in I:
        events.append((a,1))
        events.append((b+1,-1))
    events.sort()
    max_grubosc = 0
    akt_grubosc = 0
    for km, grubosc in events:
        akt_grubosc += grubosc
        if akt_grubosc > max_grubosc:
            max_grubosc = akt_grubosc
    return max_grubosc