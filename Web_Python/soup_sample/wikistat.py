from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):

    #bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:

        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        '''images'''
        img_tags = body('img')
        count_img = 0
        for tag in img_tags:
            if int(tag['width']) > 199:
                count_img += 1
        imgs = count_img

        '''headers'''
        header_tags = body(re.compile('^h[1-6]$'))
        count_header = 0
        for i in range(len(header_tags)):
            if header_tags[i].find(string=re.compile('^[ETC]')):
                count_header += 1
        headers = count_header

        '''linkslen'''
        links = soup.find_all('a')
        max_count = 0
        for link in links:
            current_count = 1
            siblings = link.find_next_siblings()
            for sibling in siblings:
                if sibling.name == 'a':
                    current_count += 1
                    max_count = max(current_count, max_count)
                else:
                    current_count = 0
        linkslen = max_count

        '''lists'''
        lsts = body.find_all(['ul', 'ol'])
        lists = 0
        for lst in lsts:
            if not lst.find_parents(['ul', 'ol']):
                lists += 1

        out[file] = [imgs, headers, linkslen, lists]

    return out
