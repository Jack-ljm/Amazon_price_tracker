import requests
from bs4 import BeautifulSoup
import smtplib
from easygui import msgbox
import time

#def check_import_fees(url):
 #   if (soup.find(id = 'priceblock_ourprice_ifdmsg') == None):
  #      return -1
   # else: return 1
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('','')
    subject = 'THE PRICE FELL DOWN!!'
    body = 'Check on the links https://www.amazon.ca/gp/product/B073JHHNJ9/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('mailtester88888@gmail.com','jliu1415705090@gmail.com',msg)
    print('Email has been sent')
    server.quit()

def check_price():

    URL = 'https://www.amazon.ca/gp/product/B073JHHNJ9/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1'
#url = 'https://www.amazon.ca/Adapter-AC1300Mbps-802-11Ac-Wireless-Desktop/dp/B07MJYYGCV?pf_rd_p=fa7257ba-c43b-495b-9a20-f1fcc5d85a68&pd_rd_wg=vdVm2&pf_rd_r=533WB9ENX3WKD8CQ3G2Z&ref_=pd_gw_cr_simh&pd_rd_w=LEsPf&pd_rd_r=bbf2a047-19cd-4cbd-8501-97aed19ad529'
    header = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

    page = requests.get(URL, headers= header)
    soup = BeautifulSoup(page.content,'lxml')
    title = soup.find(name = 'title').get_text()
    price = (soup.find(id = 'priceblock_ourprice' ).get_text())[5:10]   
    price_conveted = float(price)
# Need a function to detect is there's a importing fee or not.
    if (price_conveted >65):
        send_email()
        msgbox('DUDE,CHECK YOUR EMAIL',"WOW",'Indeed','./sob.jpg')
    #importing_exist = check_import_fees(URL)
    #print(importing_exist)
    #if importing_exist == 1:
        #importing_fees = soup.find(id = 'priceblock_ourprice_ifdmsg').get_text()[0:12]
while(1):
    check_price()
    time.sleep(3600)



