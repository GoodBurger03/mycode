     #!/usr/bin/env python3
import re
import urllib.request

print("where should we search?")
url = input()

print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")

searchFor = input()

searchMe = urllib.request.urlopen(url).read().decode("utf-8")

cont = input()

def main():
    if re.search(searchFor, searchMe):
     print("Found a match!")
    else:
        print("No match!")



print("Did you want to try another ?" + str(cont))

 if cont.lower == "yes":
  main()
  else:
  print("have a nice day")
  break


main()
