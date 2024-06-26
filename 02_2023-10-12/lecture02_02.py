#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    # lecture02_data.xmlと同じ内容のbookツリーを新規作成しxmlファイルに書き出す関数
    root = ET.Element("book")
    
    article = ET.SubElement(root, "article")
    article.attrib['title'] = "卒業論文"
    
    chapters = ({"id":"1", "name":"はじめに", "pages":"2"},
                {"id":"2", "name":"基礎理論", "pages":"8"},
                {"id":"3", "name":"実験方法", "pages":"6"},
                {"id":"4", "name":"結果と考察", "pages":"2"},
                {"id":"5", "name":"まとめ", "pages":"1"},
                {"id":"6", "name":"参考文献", "pages":"2"}
            )
    
    for i in chapters:
        chapter = ET.SubElement(article, "chapter")
        for j in i.keys():
            chapter.attrib[j] = i[j]
    
    
    novel = ET.SubElement(root, "novel")
    
    chapters = ({"id":"1", "name":"1日のはじまり", "pages":"2"},
                {"id":"2", "name":"朝食", "pages":"8"},
                {"id":"3", "name":"仕事", "pages":"6"},
                {"id":"4", "name":"帰宅後", "pages":"2"},
                {"id":"5", "name":"新しい朝", "pages":"1"}
            )
    
    for i in chapters:
        chapter = ET.SubElement(novel, "chapter")
        for j in i.keys():
            chapter.attrib[j] = i[j]
    
    
    with open("lecture02_02_data.xml", 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))

    

if __name__ == '__main__':
    lecture02_02()