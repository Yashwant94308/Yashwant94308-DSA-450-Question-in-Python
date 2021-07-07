rideDuration = 50
songDuration = [1, 2, 3, 4, 5, 6, 7, 8]


def pair(d, song):
    ed = d - 30
    hm = {}
    res = []
    for i in range(len(song)):
        if song[i] in hm:
            res.append([hm[song[i]], i])
        else:
            hm[ed - song[i]] = i
    print(res)


pair(rideDuration, songDuration)
