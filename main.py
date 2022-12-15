import re

pattern = r".*z.{3}z.*"
file = open('z3z.txt','r')
while True:
  line = file.readline()
  if re.search(pattern, line) is not None:
    print(line)
  if not line:
    break