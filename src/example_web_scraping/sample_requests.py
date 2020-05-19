import requests


def get_html(url):
    r = requests.get(url)
    return r.text


def main():
    url = 'https://www.youtube.com/user/PavelVolyaOfficial/videos?disable_polymer=1'
    # print(get_html(url).encode('cp1251', 'replace').decode('cp1251'))
    print(get_html(url))


if __name__ == '__main__':
    main()
