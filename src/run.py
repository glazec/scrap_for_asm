from jiandan import jiandan
from shuaia import shuaia
from asm_hentai import asm_hentai
from sys import exit

while True:
    j = input("18x or 10x or any key to quit(18/10):\n")
    if j == "10":
        k = input("shuai'ge or beauty?(s or b):\n")
        if k == "s":
            shuaia()
        else:
            jiandan()
    elif j == "18":
        asm_hentai()
    else:
        exit(0)


