from meteostat import Point, Daily

def task(row):
    try:
        #out = list(arg)
        #idx = out[0][0]
        #row = out[0][1]
        start = end = row[1][0]
        print(start)
        location = Point(row[1][11], row[1][12])
        print(location)
        data = Daily(location, start, end)
        data = data.fetch()
    except Exception:
        pass
    
    try:
        row[1][13] = data.tavg[0]
    except Exception:
        pass
    try:
        row[1][14] = data.prcp[0]
    except Exception:
        pass
    try:
        row[1][15] = data.snow[0]
    except Exception:
        pass
    try:
        row[1][16] = data.wspd[0]
    except Exception:
        pass
    try:
        row[1][17] = data.pres[0]
    except Exception:
        pass
    
    return(row[1])
        