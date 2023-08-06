# -*- coding: GBK -*-

import sys
import os

from docx2python import docx2python
from pathlib import Path
import regex
import re

import pandas as pd
import numpy as np

from .regex_dictionary import get_chapter_beg_end
from .regex_dictionary import get_chapter_regex
from .regex_dictionary import get_section_beg_end
from .regex_dictionary import get_section_regex

class Contract:
    def __init__(self, path):
        print(path)
        self.exp = '(��̩)|(����)(?!����)|(����)(?!��Ͷ)|(����)|(�㷢)|(��ͨ)|(����)|(���)|(ƽ��)|(����)|(��ҵ)|(����)|(��)(?:����)(��)|(��Ͷ)'
        self.path = path
        self.product_name = regex.search('(����|����).+?����', path).group()
        self.document = docx2python(path)
        self.full_text = ''
        for table in self.document.body:
            for row in table:
                for cell in row:
                    for para in cell:
                        self.full_text += para
        try:
            self.tg = ''.join(filter(None,regex.search(self.exp, path).groups()))
        except:
            self.tg = ''

    def get_front_page(self):
        firstpages = {"���":25,"ƽ��":25,"����":28,"��ͨ":18,"����":22,"����":19,"�㷢":0,"����":25,"����":28,"��̩":23}
        return firstpages[self.tg]

    def get_risk_level(self):
        try:
            return re.search("R[0-9]",re.search("����������[^��]+�ϸ�Ͷ����", self.full_text).group()).group()
        except:
            return ""

    def get_full_text(self):
        return self.full_text

    def get_chapter(self, chapter): #works
        beg_chapter_name = get_chapter_beg_end(self.tg, chapter)[0][0]
        end_chapter_name = get_chapter_beg_end(self.tg, chapter)[0][1]
        chapter_regex = get_chapter_regex(self.tg, beg_chapter_name, end_chapter_name)
        try:
            self.chapter = regex.search(chapter_regex, self.full_text).group()
            return self.chapter
        except:
            return 'No Regex Matches'
            
    def get_section_of_chapter(self, chapter, section):
        chapter = self.get_chapter(chapter)
        
        if self.tg=='����':
            beg_section_name1 = get_section_beg_end('����1', section)[0][0]
            end_section_name1 = get_section_beg_end('����1', section)[0][1]
            beg_section_name2 = get_section_beg_end('����2', section)[0][0]
            end_section_name2 = get_section_beg_end('����2', section)[0][1]
            self.section_regex = '({}|{})'.format(get_section_regex('����', beg_section_name1, end_section_name1),\
                get_section_regex('����', beg_section_name2, end_section_name2))
        elif self.tg=='����':
            beg_section_name1 = get_section_beg_end('����1', section)[0][0]
            end_section_name1 = get_section_beg_end('����1', section)[0][1]
            beg_section_name2 = get_section_beg_end('����2', section)[0][0]
            end_section_name2 = get_section_beg_end('����2', section)[0][1]
            beg_section_name3 = get_section_beg_end('����3', section)[0][0]
            end_section_name3 = get_section_beg_end('����3', section)[0][1]
            self.section_regex = '({}|{}|{})'.format(get_section_regex('����', beg_section_name1, end_section_name1),\
                get_section_regex('����', beg_section_name2, end_section_name2),get_section_regex('����', beg_section_name3, end_section_name3))
        else:
            beg_section_name = get_section_beg_end(self.tg, section)[0][0]
            end_section_name = get_section_beg_end(self.tg, section)[0][1]
            self.section_regex = get_section_regex(self.tg, beg_section_name, end_section_name)

        try:
            self.section = regex.search(self.section_regex, chapter).group()
            if self.section[0] == '��':
                self.section = self.section.replace('��','')
            return self.section
        except:
            return 'No Regex Matches'
    
    def get_section_regex(self, section):
        if self.tg=='����':
            beg_section_name1 = get_section_beg_end('����1', section)[0][0]
            end_section_name1 = get_section_beg_end('����1', section)[0][1]
            beg_section_name2 = get_section_beg_end('����2', section)[0][0]
            end_section_name2 = get_section_beg_end('����2', section)[0][1]
            self.section_regex = '({}|{})'.format(get_section_regex('����', beg_section_name1, end_section_name1),\
                get_section_regex('����', beg_section_name2, end_section_name2))
        elif self.tg=='����':
            beg_section_name1 = get_section_beg_end('����1', section)[0][0]
            end_section_name1 = get_section_beg_end('����1', section)[0][1]
            beg_section_name2 = get_section_beg_end('����2', section)[0][0]
            end_section_name2 = get_section_beg_end('����2', section)[0][1]
            beg_section_name3 = get_section_beg_end('����3', section)[0][0]
            end_section_name3 = get_section_beg_end('����3', section)[0][1]
            self.section_regex = '({}|{}|{})'.format(get_section_regex('����', beg_section_name1, end_section_name1),\
                get_section_regex('����', beg_section_name2, end_section_name2),get_section_regex('����', beg_section_name3, end_section_name3))
        else:
            beg_section_name = get_section_beg_end(self.tg, section)[0][0]
            end_section_name = get_section_beg_end(self.tg, section)[0][1]
            self.section_regex = get_section_regex(self.tg, beg_section_name, end_section_name)
        print(self.section_regex)
        
    # def to_pdf(): #under construnction, same as Contracts method, but only exports pdf of one contract document

class Contracts:
    def __init__(self, folder_path):
        self.exp = '(��̩)|(����)(?!����)|����|(����)(?!��Ͷ)|(����)|(�㷢)|(��ͨ)|(����)|(���)|(ƽ��)|(����)|(��ҵ)|(����)|(��)(?:����)(��)|(��Ͷ)'
        self.folder_path = folder_path
        self.all_files = []
        self.tg = []
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for name in files:
                path = os.path.join(root, name)
                if ('output' not in path) and ('docx' or 'doc' in path) and ('����Э��' not in path):
                    try:
                        self.tg.append(''.join(filter(None,regex.search(self.exp, path).groups())))
                        self.all_files.append(path)
                    except:
                        print('Ŀǰֻ֧�֣���̩|����|���Ž�Ͷ|����|�㷢|��ͨ|����|���|ƽ��|����|��ҵ|����|��Ͷ��word�ĵ��������йܵĲ�Ʒ���ᱻ���ԡ�')
                else:
                    pass
    def get_chapters(self, chapter_names):
        out = {}
        for file_path in self.all_files:
            contract = Contract(file_path)
            if contract.tg!='�㷢': out[contract.product_name] = [contract.get_chapter(chapter_name).replace('\t', ' ').replace('\n', '') for chapter_name in chapter_names]
        return out, chapter_names
    
    def get_sections(self, chapter_name, section_names):
        out = {} #dict(per tg) of list(per product) of list(per regex expression)
        for file_path in self.all_files:
            contract = Contract(file_path)
            if contract.tg!='�㷢': out[contract.product_name] = [contract.get_section_of_chapter(chapter_name, section_name).replace('\t', ' ').replace('\n', '') for section_name in section_names]
        return out, section_names

    def get_sections_regex(self, section_names):
        for file_path in self.all_files:
            contract = Contract(file_path)
            contract.get_section_regex(section_names)
        
    def get_df(self, dict):
        data = dict[0]
        names = list(data.keys())
        matrix = np.array([data[product] for product in names])
        df = pd.DataFrame(matrix, index=[names], columns=list(dict[1]))
        return df
    
    def to_excel(self, df, out_path):
        abs_path = Path(out_path).absolute()
        df.to_excel(out_path)
        print(f'Spreadsheet successfully exported to {abs_path}.')
        return df

    # def to_pdf(self, regex): under construction, to include functions from strategy_extract to export pdf of only regexed contents

# in_path = sys.argv[1]
# out_path = sys.argv[2]
# chapter = sys.argv[3]
# sections = list(sys.argv[4:])

# def main():
#     contracts = Contracts(in_path)
#     contracts.to_excel(contracts.get_df(contracts.get_sections(chapter, sections)), out_path) # works

# if __name__=='__main__':

    ### single contract class
    # contract = Contract('/Users/andy/Desktop/work/ubiquant/��ͬ��ȡ/��ҳ��Ͷ�ʲ�����ȡ/����/�������׾�ѡ2��˽ļ֤ȯͶ�ʻ�������ͬ�йܰ�-���ݵ�һ�β���Э����£�Ͷ�ʶ˺����£�V1.2.8TX-20210302�����壩.docx')
    # print(contract.get_chapter('�����Ͷ��'))
    # print(contract.get_section_of_chapter('�����Ͷ��','Ͷ������'))

    ### folder of contracts class
    
    # main()