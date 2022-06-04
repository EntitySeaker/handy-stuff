import requests
import sys

def main():
  if len(sys.argv) > 1:
    r = requests.get(f"https://ipapi.co/{sys.argv[1]}/json/")
  else:
    r = requests.get(f"https://ipapi.co/json/")
  print(r.text)

if __name__ == '__main__':
  main()
