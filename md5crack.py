#!/bin/python3
# Url = https://www.cellphonetrackers.org/tool/mac.php?md5=5f4dcc3b5aa765d61d8327deb882cf99

import sys
import requests

def main():
  url = "https://www.cellphonetrackers.org/tool/mac.php?md5="
  hash = sys.argv[1]
  print(f"Cracking password {hash}")
  r = requests.get(url+hash)
  data = r.text.split("<font color=red>")[1].split("</font>")[0].replace("$HEX[","").replace("]","")
  if data != " 1020":
    print(bytearray.fromhex(data).decode().replace("\n",""))
  else:
    print("Hash not in tables!")

if __name__ == "__main__":
  main()
