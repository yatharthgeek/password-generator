print("""
█▀█ ▄▀█ █▀ █▀ █░█░█ █▀█ █▀█ █▀▄   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀█ ▄█ ▄█ ▀▄▀▄▀ █▄█ █▀▄ █▄▀   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄ V1.0 
""")

import random

uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
num="0123456789"

unit=lower+uppercase+num
pwdlen=int(input("Length of Password >> "))

pwd="".join(random.sample(unit,pwdlen))

print(pwd)
