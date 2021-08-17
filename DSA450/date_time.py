from datetime import datetime as dt, timedelta as td

dic = dict()
def main():

    n = int(input())
    while n > 0:
        start, end = [str(i) for i in input().split()]
        sd = dt.strptime(start, '%Y-%m-%d')
        ed = dt.strptime(end, '%Y-%m-%d')
        sd = sd.date()
        ed = ed.date()-td(days=1)
        delta = ed - sd

        for i in range(delta.days + 1):
            if str(sd + td(days=i)) in dic:
                dic[str(sd + td(days=i))] += 1
            else:
                dic[str(sd + td(days=i))] = 1
        n -= 1
    mk = ''
    mv = 0
    # print(dic)
    for k, v in dic.items():
        if v > mv:
            mv = v
            mk = k
    print(mk)


if __name__ == '__main__':
    main()