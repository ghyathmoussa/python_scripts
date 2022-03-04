import pandas as pd
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
    for i in body_td:
        if len(i) == 0:
            body_td.remove(i)
        count = 0
    for i in body_td:
        for j in i:
            j.replace('\n','')
    body_td_fin = []
    new_item = []
    for i in body_td:
        new_item = [x[:-1] for x in i]
        body_td_fin.append(new_item)
    for i in body_td_fin:
        for j in i:
            if j == '':
                i.remove(j)
    for i in body_td_fin:
        print(len(i))
    data = pd.DataFrame(data=body_td_fin,columns=head_list)
    name = input('set the of file: ')
    data.to_excel(f'{name}.xlsx')
