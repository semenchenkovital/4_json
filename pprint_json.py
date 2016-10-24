#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs

def load_data(filepath):
    infile=codecs.open(filepath,'r', 'utf-8-sig').read()
    jsondata = json.loads(infile)
    return jsondata

def pretty_print_json(data):
    len_data = len(data)
    i = 0
    while i<len_data:
       print(json.dumps(data[i], ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')))
       i = i+1
if __name__ == '__main__':
     file = input("Введите имя файла:")
     try:
       data = load_data(file)
     except:
       print('Некорректное имя файла или путь к файлу')
     else:
         pretty_print_json(data)
