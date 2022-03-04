from inspect import BoundArguments
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

with open('pharm.html', encoding='UTF-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    tag = soup.table  # script the table
    thead = tag.thead.tr  # script th from table
    th_list = list(thead)  # convert th tags into list
    head_list = []
    # append th text to list

    for th in th_list:
        head_list.append(th.text)
    print(len(head_list))
    # get th body of table
    tbody = tag.tbody
    body_tr_list = [] # to save the tr tag
    body_td = [] # to save td tags text
    for tr in tbody:
        tr = list(tr)
        body_tr_list.append(tr)
    for tr in body_tr_list:
        body_td_text = []
        if len(tr) > 1:
            for td in tr:
                body_td_text.append(td.text)
        body_td.append(body_td_text)

    # data = pd.DataFrame(data=body_td,columns=head_list)
    # name = input('set the of file: ')
    # data.to_excel(f'{name}.xlsx')
