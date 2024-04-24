from bs4 import BeautifulSoup

with open('CGPA.html','r') as html_file:
    content=html_file.read()
    
    soup = BeautifulSoup(content,'lxml')
    course = soup.find_all('div', class_ = 'form-group')
    for c in course:
        print(c.p)
    # print(soup.prettify())
    # tags= soup.find_all('button')
    # print(tags)
    # for t in tags:
    #     print(t.text)