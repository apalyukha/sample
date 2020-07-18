import pyshorteners


url = pyshorteners.Shortener()
print("Скорочений URL - ", url.tinyurl.short(
    'https://www.lohika.com.ua/vacancy/803b2651-798d-485c-ac5c-6896c0740761'
))
