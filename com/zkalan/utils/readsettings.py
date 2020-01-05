# -*- coding: utf-8 -*-

from configparser import ConfigParser


def get_all_config():
    cp = ConfigParser()
    cp.read('settings.cfg')

    sections = cp.sections()
    item_dic = {}
    for section in sections:
        temp_list = cp.items(section)
        for i in range(temp_list.__len__()):
            item_dic[temp_list[i][0]] = temp_list[i][1]
    return item_dic


if __name__ == '__main__':
    print(get_all_config())
