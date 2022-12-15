import requests
from bs4 import BeautifulSoup
def number():
    web=requests.get("https://invoice.etax.nat.gov.tw/")    
    web.encoding = 'utf-8'
    soup = BeautifulSoup(web.text, "html.parser")

    div=soup.find_all("div",class_="etw-web")
    div=div[1]

    table=div.find_parent().find_all('tbody')
    table=table[0]

    tr=table.find_parent().find_all('tr')

    td=[]
    for i in tr[1:4]:
        td.append( i.find('td',headers="th02") )
    p=[]
    for i in td:
        p.append(i.find_parent().find_all('p',class_="etw-tbiggest"))
    num_spacial_award=p[0][0].get_text()
    num_spacial=p[1][0].get_text()
    num_big_award=[]
    for i in p[2]:
        num_big_award.append(i.get_text()[1:])
    num=[]
    num.append(num_spacial_award)
    num.append(num_spacial)
    num.append(num_big_award)
    return num
