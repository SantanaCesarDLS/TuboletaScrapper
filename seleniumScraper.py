from selenium import webdriver
from bs4 import BeautifulSoup as bs
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email(eventID):
    content = str(MIMEText(u'<a href="https://www.uepatickets.com/Wizard/Default.aspx?id='+ eventID +'#step-1">link</a>','html'))
    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login('c300698@gmail.com','Nozeteolvide34@')
    mail.sendmail('c300698@gmail.com','c300698@icloud.com',content)
    mail.close()



def EventChecker(EventName):
    url = "https://eventos.tuboleta.com.do"
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.execute_script("return document.documentElement.outerHTML")

    web_soup = bs(html,'html.parser')   
    web_soup =web_soup.find('div',{'class': 'featured-items'})
    web_soup.findAll('h2',{'class': 'notranslate'})
    Events_dict = {}
    driver.quit()
    for event in web_soup:
        event_name =event.find('a')
        if(len(str(event_name))  > 2):
            event_id = event_name["href"]
            Events_dict[event_name.string] = event_id
        

    if EventName in Events_dict:
        email(Events_dict[EventName])
        print(str(Events_dict[EventName]))
        driver.quit()
    else:
        print('Not Found')
        EventChecker(EventName)


print(str(EventChecker('J Balvin')))
