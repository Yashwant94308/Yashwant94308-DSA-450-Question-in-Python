def queries(T, Q, query):
    list = [0]
    # Suppose we have inserted 6, 3, 2 in the list and then xor everything with 4, 5,
    #    then it is same as XOR-ing with X = XOR(4,5).

    # For   Query 1, XOR with request[i].
    # with  xi.instead, we will just update X = XOR(x, xi)

    X = 0  # total xor so far

    for request in query:
        if request[0] == "0":
            # Insert in list —>for Query 0 : dont insert num in list, but we will insert number xor X (is
            # ensures that when print the whole list, it will cancel out the previous XORs.
            # so our list will contain for the 2nd example {0,6,3,(3 XOR(4)),}
            list.append((int(request[1]) ^ X))  #
        else:  # Its one perform xor on all items in query ^
            X = X ^ int(request[1])

    # . we will XOR all with the final X var
    list = [i ^ X for i in list]
    list.sort()
    print(list)


queries(1, 5, ["04", "02", "14", "05", "18"])  # [8, 12, 13, 14]
queries(1, 5, ["06", "03", "02", "14", "03", "15", "12"])  # [0, 1, 3, 4, 5]
