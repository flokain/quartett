import os
from typing import Dict

print(os.getcwd())

import xml.etree.ElementTree as ET

tree = ET.parse('./resourcen/template.svg')
root = tree.getroot()

namespaces = {'svg': 'http://www.w3.org/2000/svg',
              'xlink': "http://www.w3.org/1999/xlink"}

fieldSelectors = {"card_name": {'xpath': ".//*[@id='%s']/svg:tspan"},
                  "card_subtitle": {'xpath': ".//*[@id='%s']/svg:tspan"},
                  "category_": {'xpath': ".//*[@id='%s']/svg:tspan"},
                  "val_": {'xpath': ".//*[@id='%s']/svg:tspan"},
                  "val_bar_": {'xpath': ".//*[@id='%s']"},
                  "description": {'xpath': ".//*[@id='%s']/svg:flowPara"},
                  "top_right_text": {'xpath': ".//*[@id='%s']/svg:tspan", 'element': ''},
                  "top_right_img": {'xpath': ".//*[@id='%s']", 'element': 'href'},
                  "main_img": {'xpath': ".//*[@id='%s']", 'element': 'href'},
                  "background_img" : {'xpath': ".//*[@id='%s']", 'element': 'href'}
                  }

fields = {}

for name, selector  in fieldSelectors.items():
    xpath = selector['xpath']
    if name[-1] == '_':
        for i in range(1, 5):
            n = name + str(i)
            x = xpath % (n)
            fields[n] = root.find(x, namespaces)
    else:
        x = xpath % (name)
        fields[name] = root.find(x, namespaces)

for name,selector in fields.items():
        print(name,selector)