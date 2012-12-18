#!/usr/bin/env python

import sys
from xml.dom.minidom import Document
import yaml


def process_list(dom_el, par_el, lst):
    if par_el.tagName == 'contains' or par_el.tagName == 'anchors':
        tag_name = 'contained'
    else:
        tag_name = 'type'
    for m in lst:
        el_3 = dom_el.createElement(tag_name)
        el_3.setAttribute('urn', m)
        par_el.appendChild(el_3)
    return

def make_xml_doc():
    new_doc = Document()
    el = new_doc.createElement('aristotle_demo_suite')
    new_doc.appendChild(el)
    return new_doc

def split_name(string):
    return string.split(':')

def convert_yaml(new_dom, yaml_dict):
    for i in yaml_dict:
        sn = split_name(i)
        # tag = sn[-1]
        tag = 'resource'
        el = new_dom.createElement(tag)
        el.setAttribute('urn', i)
        query_dict = yaml_dict[i]['q']
        for n in query_dict:
            sn_2 = split_name(n)
            el_2 = new_dom.createElement(sn_2[-1])
            el_2.setAttribute('urn', n)
            try:
                t = query_dict[n].encode('ascii', 'ignore')
                text_el = new_dom.createTextNode(t)
                el_2.appendChild(text_el)
            except:
                process_list(new_dom, el_2, query_dict[n])
            el.appendChild(el_2)
        new_dom.firstChild.appendChild(el)
    return new_dom

def write_xml(doc):
    with open(sys.argv[2], "w") as f:
        f.write(doc.toprettyxml())

def read_yaml():
    f = open(sys.argv[1])
    yml = yaml.load(f.read())
    f.close()
    return yml

def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    yaml_dict = read_yaml()
    x = convert_yaml(make_xml_doc(), yaml_dict)
    write_xml(x)
    print x.toprettyxml()
    return

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print "Usage: CCSSyaml2xml.py [input file] [output file]"
