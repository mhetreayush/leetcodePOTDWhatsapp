from datetime import datetime, date
import requests
import re
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
sid = os.getenv("SID")
authToken = os.getenv("authToken")
to= os.getenv("to")
from_ = os.getenv("from_")

client = Client(sid, authToken)

month = datetime.now().strftime("%b")
dateNumber = str(date.today()).split("-")[2]
requiredDate = month+" "+dateNumber

r = requests.get("https://leetcode.com/problemset/all/")
result = r.text
index = result.find(requiredDate)

href = result[index: index+200]
result = re.search('href=(.*)target', href)

problemUrl = "https://leetcode.com"+result.group(1).replace("\"", "")

message = client.messages.create(
    to=to, from_=from_, body=problemUrl)
