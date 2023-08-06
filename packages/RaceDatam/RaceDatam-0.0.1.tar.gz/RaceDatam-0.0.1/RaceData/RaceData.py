import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

def datadf(start,page,pagesize):

        headers = {
        'authority': 'www.runbritain.com',
        'accept': '*/*',
        'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'RBCookieCheck=n; _ga=GA1.2.1379117210.1664101633; _gid=GA1.2.611527774.1664101633; AWSALB=/7h1mMAloqs0zcuMhit0xF9Ot7rcvaIhVZJEt5CJ/L0lzzolOZvbFmy6u8XZbRjXpFrcicDSrH5YjkNH/bzDSN4x8iQ/RVyQdFXfTTLnQLSjLKx6Ov7wZnXVhHVl; AWSALBCORS=/7h1mMAloqs0zcuMhit0xF9Ot7rcvaIhVZJEt5CJ/L0lzzolOZvbFmy6u8XZbRjXpFrcicDSrH5YjkNH/bzDSN4x8iQ/RVyQdFXfTTLnQLSjLKx6Ov7wZnXVhHVl',
        'referer': 'https://www.runbritain.com/races',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-newrelic-id': 'UgQBWVNWGwUCXVNbDwg=',
        'x-requested-with': 'XMLHttpRequest',
    }
        cookies = {
        'RBCookieCheck': 'n',
        '_ga': 'GA1.2.1379117210.1664101633',
        '_gid': 'GA1.2.611527774.1664101633',
        'AWSALB': '/7h1mMAloqs0zcuMhit0xF9Ot7rcvaIhVZJEt5CJ/L0lzzolOZvbFmy6u8XZbRjXpFrcicDSrH5YjkNH/bzDSN4x8iQ/RVyQdFXfTTLnQLSjLKx6Ov7wZnXVhHVl',
        'AWSALBCORS': '/7h1mMAloqs0zcuMhit0xF9Ot7rcvaIhVZJEt5CJ/L0lzzolOZvbFmy6u8XZbRjXpFrcicDSrH5YjkNH/bzDSN4x8iQ/RVyQdFXfTTLnQLSjLKx6Ov7wZnXVhHVl',
    }
        
        response = requests.get('https://www.runbritain.com/handlers/RaceHandler.ashx?keyword=&month=&datefrom='+str(start)+'&dateto='+str(start)+'&distance=&region=&county=&profile=&raceType=&awards=&entrants=&page='+str(page)+'&pagesize='+str(pagesize)+'&gender=0&onlineentry=0&responseType=html', cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
    
        races = soup.find_all("div", {'class':['race', 'race last']})

        mydata = []

        for race in races:
            
            race_date = race.find('time')['datetime']
            txts=soup.find_all('div', class_='description')
            
            for txt in txts:
                
                try:
                    race_name = txt.find('h2').text
                    city=txt.find('ul', class_='list').find('li').text
                    name_phone=txt.find('ul', class_='list').findNext('li').findNext('li').text
                    distance=txt.find('ul', class_='distance').findNext('li').text.replace(' km','').replace('Distance:' ,'')
                    flat=txt.find('ul', class_='distance').findNext('li').findNext('li').text
                    Road=txt.find('ul', class_='distance').findNext('li').findNext('li').findNext('li').text
                    Field=txt.find('ul', class_='distance').findNext('li').findNext('li').findNext('li').findNext('li').text.replace('Field: ','')
                    Start=txt.find('ul', class_='distance').findNext('li').findNext('li').findNext('li').findNext('li').findNext('li').text.replace('Start: ','')
                    weblink=txt.find('div', class_='web-link').find('span').find('a')['href']
                    licence=txt.find('div', class_='licence').find('p').text.replace('Licence No: ','')
                    licence_status =txt.find('ul', class_='btn-list').findNext('li').findNext('li').find('a').text


                    veri ={

                    'race_date':race_date,
                    'race_name':race_name,
                    'city':city,
                    'name_phone':name_phone,
                    'distance':distance,
                    'flat':flat,
                    'Road':Road,
                    'Field':Field,
                    'Start':Start,
                    'weblink':weblink,
                    'licence':licence,
                    'licence_status':licence_status,


                     }
                    
                    mydata.append(veri)
                except:
                    
                    pass
                
                
                df = pd.DataFrame(mydata)

            return df

        
def dataal():
    
        print('Tarih formatı "25/09/2022" şeklinde olmalıdır.')
        print('Lütfen Tarih Aralığını 30 gün ile sınırlı tutunuz.')

        d1 = input('Baslangıc Tarihi Giriniz:   ')
        d2 = input('Bitiş Tarihi Giriniz:   ')
            
        df = pd.DataFrame()
            
        date1 = datetime.date(int(d1.split('/')[2]), int(d1.split('/')[1]), int(d1.split('/')[0]))
        date2 = datetime.date(int(d2.split('/')[2]), int(d2.split('/')[1]), int(d2.split('/')[0]))
            
        day = datetime.timedelta(days=1)

        while date1 <= date2:
                print(date1.strftime('%d/%m/%Y'))
                date1 = date1 + day
                
                for i in range(5):
                
                    
                    print('{} tarihi için {} sayfa taranıyor'.format(date1,i))
                    sonuc = datadf(str(date1),i,100)
                   

                    if sonuc is not None:
                        df = pd.concat([df,sonuc])
                    else:
                        break

        df1 = df.drop_duplicates()            
        df1.to_excel('RaceDataExcel.xlsx')
        df1.to_csv('RaceDatacsv.csv')
        print('Verileriniz "RaceDataExcel" olarak masaüstününde oluştu')
        print('İşlem Sonuçlandı')
                        
                
            



        

    
        

    
    

    
     
 





