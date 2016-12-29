from bs4 import BeautifulSoup
import requests
import re

result = requests.get("https://stackoverflow.com/users/login?ssrc=head")
c=result.content
soup = BeautifulSoup(c, "lxml")
samples = soup.select(r"#login-form > input[type=\"hidden\"]")
fkey = samples[0].attrs['value']
# m = re.search(r"value=.*", fkey)
# print m.group(1)
