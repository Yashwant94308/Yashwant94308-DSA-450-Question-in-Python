def search(pat, txt, q):
    d = 256
    m = len(pat)
    n = len(txt)

    j = 0
    h = 1
    p = 0  # hash of pat
    t = 0  # hash of txt

    # The value of h would be "pow(d, M-1)%q"

    for i in range(m - 1):
        h = (h * d) % q

    for i in range(m):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    for i in range(n - m + 1):
        if p == t:
            while j < m:
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
            if j == m:
                print("index at", i+1)
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q
            if t < 0:
                t += q


text = "3343343334333433334333334333334333343333433334"
patt = "334"

# A prime number
qq = 101

# Function Call
search(patt, text, qq)
