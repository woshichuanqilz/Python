import requests
import re
from bs4 import BeautifulSoup
url = "https://stackoverflow.com/users/login?ssrc=head"
USERNAME = '513278236@qq.com'
PASSWORD = 'woshichuanqilz72'

with requests.Session() as c:
    res = c.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    samples = soup.select(r"#login-form > input[type=\"hidden\"]")
    fkey = samples[0].attrs['value']
    print fkey

    login_data = dict(fkey=fkey, username=USERNAME, password=PASSWORD)
    c.post(url, data=login_data)
    page = c.get("https://stackoverflow.com")
    print page.content
