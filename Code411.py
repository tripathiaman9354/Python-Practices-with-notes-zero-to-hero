import os
if os.path.exists("demofile4.txt"):
  os.remove("demofile4.txt")
else:
  print("The file does not exist")