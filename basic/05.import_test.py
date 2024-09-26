import time  # inner module
import requests  # pip install requests (in console), not in this python version

print("start")
time.sleep(2)
print("end")

# fetch web content
response = requests.get("http://www.example.com/")
print(response)


# pip install -i XXXX
# XXXX any mirror like tsinghua...
