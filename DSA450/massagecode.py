import requests
import json
import pandas as pd


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        # 'authorization': 'A0IZEKsizwFx7dpB9W1MNUDamgQYchPeL54oq8RnC3TG2uOvX6oVcfYdyH30AL1iBlGXxbEIFaQJUvOW',
        # 'authorization': 'ue4vDyf3750OUlonc2d1YT9prmVAxHMbGKgqjaXRFLJ8NSCwhIATQn9c7Cj2dDaLNpEkKs1mJrxBM6vt',
        'authorization': 'b2dURI5OcQKSfMFpqJ74grjw9nhvlazHY1PetGC8Voi3XxT6Dm4EpohJfkA6rcuz9gdRmwDjsaGCXi08',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')

k = 0
df = pd.read_csv("arunconc.csv")
for i in df.PhoneValue:
    if len(str(int(i))) == 10:
        k+= 1
        num = str(int(i))
        # msg = 'Sabko Dekha Baar Baar, Abki Baar MANOJ KUMAR, Fir Se Unko Lana Hai , MANOJ KUMAR Ko Hi MUKHIYA Banana ' \
        #       'Hai, (Panchyat-DUMARA-NUNORA, BELSAND) '
        msg = 'सबको देखा बार बार अबकी बार मनोज कुमार, फिर से उन्ही को लाना है, मनोज कुमार को ही मुखिया बनाना है। (' \
              'डुमरा - नुनौरा, बेलसंड) '
        r = send_sms(num, msg)
        if r:
            print('yes', k)
        else:
            print('No', k)
