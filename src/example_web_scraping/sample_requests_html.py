from requests_html import HTMLSession

session = HTMLSession()

url = 'https://support.foxtrotalliance.com/hc/en-us'
r = session.get(url)

print(r.text)

r.close()
session.close()
