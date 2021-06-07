import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror


def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        # 'authorization': 'A0IZEKsizwFx7dpB9W1MNUDamgQYchPeL54oq8RnC3TG2uOvX6oVcfYdyH30AL1iBlGXxbEIFaQJUvOW',
        # 'authorization': 'ue4vDyf3750OUlonc2d1YT9prmVAxHMbGKgqjaXRFLJ8NSCwhIATQn9c7Cj2dDaLNpEkKs1mJrxBM6vt',
        'authorization': 'b2dURI5OcQKSfMFpqJ74grjw9nhvlazHY1PetGC8Voi3XxT6Dm4EpohJfkA6rcuz9gdRmwDjsaGCXi08',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'unicode',
        'route': 'p',
        'numbers': number
    }
    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)
    return dic.get('return')


def btn_click():
    num = textNumber.get()
    msg = textMsg.get("1.0", END)
    r = send_sms(num, msg)
    if r:
        showinfo("Send Success", "Successfully sent")
    else:
        showerror("Error", "Something went wrong..")


# Creating GUI
root = Tk()
root.title("Message Sender ")
root.geometry("400x550")
font = ("Helvetica", 22, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)
sendBtn = Button(root, text="SEND SMS", command=btn_click)
sendBtn.pack()
root.mainloop()
