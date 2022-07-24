
def refills(loc, d, m, stops,x):
    if (loc+m)>=d:
        return 0
    if stops==[] or (stops[0]-loc)> m :
        return -1-x
    last_stop=loc
    while stops!=[] and (stops[0]-loc)<=m:
        last_stop= stops[0]
        stops.pop(0)
    x+=1
    return 1 + refills(last_stop,d,m,stops,x)

if __name__ == '__main__':
    d, m, _, *stops = map(int, input().split())
    loc=0
    x=0
    print(refills(loc,d, m, stops,x))