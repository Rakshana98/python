import requests as req
from bs4 import BeautifulSoup as bs
r = req.get("http://" + 'www.amrita.edu/faculty')
soup = bs(r.text,'html.parser')
staff_name_list = soup.find_all('div',class_= 'col-md-9')
for staff_name in staff_name_list:
    staff = staff_name.find('a',href = True)
    staff_desc=staff_name.find('p')
    #print(staff_name)
    print(staff.contents[0])
    print(staff_desc.text)
