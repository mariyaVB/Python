import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
)

response = http.request('GET', 'https://twitter.com/home')
print(response.data)


# soup = BeautifulSoup(response.text, 'lxml')
#
# twitters = soup.find_all('span', class_='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3')[:10]
# print(twitters)
# for twitter in twitters:
#     print(twitter.text)



