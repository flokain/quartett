import os
from typing import Dict

print(os.getcwd())

import xml.etree.ElementTree as ET

tree = ET.parse('./resourcen/template.svg')
root = tree.getroot()

namespaces = {'svg': 'http://www.w3.org/2000/svg',
              'xlink': "http://www.w3.org/1999/xlink"}

Textelectors = {"card_name": {'xpath': ".//*[@id='%s']/svg:tspan"},
                "card_subtitle": {'xpath': ".//*[@id='%s']/svg:tspan"},
                "category_": {'xpath': ".//*[@id='%s']/svg:tspan"},
                "val_": {'xpath': ".//*[@id='%s']/svg:tspan"},
                "description_1": {'xpath': ".//*[@id='%s']/svg:flowPara"},
                "description_2": {'xpath': ".//*[@id='%s']/svg:flowPara"},
                "top_right_text": {'xpath': ".//*[@id='%s']/svg:tspan"},
                "mid_right_text": {'xpath': ".//*[@id='%s']/svg:tspan"},
                }

imgSelectors = {"top_right_img": {'xpath': ".//*[@id='%s']"},
                "mid_right_img": {'xpath': ".//*[@id='%s']"},
                "main_img": {'xpath': ".//*[@id='%s']"},
                "background_img": {'xpath': ".//*[@id='%s']"}
                }

rectSelector = {"val_bar_": {'xpath': ".//*[@id='%s']"}
                }

texts = {}
imgs = {}
rects = {}

for name, selector in Textelectors.items():
    xpath = selector['xpath']
    if name[-1] == '_':
        for i in range(1, 5):
            n = name + str(i)
            texts[n] = {}
            x = xpath % (n)
            texts[n]['field'] = root.find(x, namespaces)
    else:
        x = xpath % (name)
    texts[name] = {}
    texts[name]['field'] = root.find(x, namespaces)

print("Printing text elements")

for name, field in texts.items():
    field['field'].text += "huh"
    print(name, field['field'], field['field'].text)



for name, selector in imgSelectors.items():
    xpath = selector['xpath']
    if name[-1] == '_':
        for i in range(1, 5):
            n = name + str(i)
            imgs[n] = {}
            x = xpath % (n)
            imgs[n]['field'] = root.find(x, namespaces)
    else:
        x = xpath % (name)
    imgs[name] = {}
    imgs[name]['field'] = root.find(x, namespaces)

print("Printing imgs paths")

for name, field in imgs.items():
    field['field'].set('{http://www.w3.org/1999/xlink}href','huhu.png')
    field['field'].set('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}absref',os.getcwd() + "huhu.png")
    print(name, field['field'],
          field['field'].get('{http://www.w3.org/1999/xlink}href'),
          field['field'].get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}absref')
          )

# save as new xml
tree.write('test_generated.svg')
