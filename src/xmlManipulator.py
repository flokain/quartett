import os
from subprocess import Popen, call
from typing import Dict

print(os.getcwd())

import xml.etree.ElementTree as ET


def substituteSVG(values):
    tree = ET.parse('../resourcen/template.svg')
    root = tree.getroot()

    namespaces = {'svg': 'http://www.w3.org/2000/svg',
                  'xlink': "http://www.w3.org/1999/xlink"}

    Textelectors = {"card_name": {'xpath': ".//*[@id='%s']/svg:tspan"},
                    "card_subtitle": {'xpath': ".//*[@id='%s']/svg:tspan"},
                    "category_": {'xpath': ".//*[@id='%s']/svg:tspan"},
                    "val_": {'xpath': ".//*[@id='%s']/svg:flowPara"},
                    "top_right_text": {'xpath': ".//*[@id='%s']/svg:tspan"},
                    "mid_right_text": {'xpath': ".//*[@id='%s']/svg:tspan",'hide':'true'},
                    }

    imgSelectors = {"top_right_img": {'xpath': ".//*[@id='%s']",'hide':'true'},
                    "mid_right_img": {'xpath': ".//*[@id='%s']"},
                    "main_img": {'xpath': ".//*[@id='%s']"},
                    "background_img": {'xpath': ".//*[@id='%s']"},
                    "bar_": {'xpath': ".//*[@id='%s']"},
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
        if name in values:
            field['field'].text = values[name]
            print(name, field['field'], field['field'].text)




    for name, selector in imgSelectors.items():
        xpath = selector['xpath']
        if name == 'bar_':
            for i in range(1, 5):
                for j in range(1, 6):
                    n = name + str(i) + "_" + str(j)
                    imgs[n] = {}
                    x = xpath % (n)
                    imgs[n]['field'] = root.find(x, namespaces)
        else:
            x = xpath % (name)
            imgs[name] = {}
            imgs[name]['field'] = root.find(x, namespaces)

    for name, field in imgs.items():
        if name.find("bar_") >= 0:

            text,i,j = name.split("_")
            val = text+"_"+ str(i)
            if val in values and int(j) > int(values[val]):
                parent= root.find(".//*[@id='"+ name +"']/..",namespaces)
                parent.remove(field["field"])

        if name == "mid_right_img":
            if values["mid_right_text"]=="":
                parent = root.find(".//*[@id='" + name + "']/..", namespaces)
                parent.remove(field["field"])


        else:
            if name in values:
                field['field'].set('{http://www.w3.org/1999/xlink}href','../../resourcen/'+values[name])
                field['field'].set('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}absref',os.getcwd()+'/../resourcen/'+values[name])
            print(name, field['field'],
                  field['field'].get('{http://www.w3.org/1999/xlink}href'),
                  field['field'].get('{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}absref')
                  )



    return tree


def renderAsPdf(svgTree, name):
    #  as new svg
    tmp_file = name + '.svg'
    pdf_file = name + '.pdf'
    tmp_dir = '../out/tmp/'
    pdf_dir = '../out/pdf/'

    for dir in [tmp_dir, pdf_dir]:
        if not os.path.exists(dir):
            os.makedirs(dir)

    svgTree.write(tmp_dir + tmp_file)

    # convert to pdf
    x = Popen(['inkscape', tmp_dir + tmp_file, \
               '--export-pdf=%s' % pdf_dir + pdf_file])