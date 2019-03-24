# coding: utf-8
import requests, re, csv
from bs4 import BeautifulSoup


def getDailyByYear(year) :
    req = requests.get(
        'https://lectionary.library.vanderbilt.edu/daily.php?year=' + year
    )
    if req.status_code != 200:
        return False

    content = BeautifulSoup(req.text, 'html.parser')

    with open('data_' + year + '.csv', mode='w') as csv_file:
        csv_write = csv.writer(
            csv_file, delimiter=';',
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL
        )
        # get weeks
        for dailys in content.select('ul.daily_day'):
            # get days
            for day in dailys.select('li'):
                li = day.find_all('strong')
                # is sunday or special day
                if len(li) > 1:
                    urlText = day.find('a').get('href')

                    line = re.findall(r"^(.*?), (.*?): (.*)$",day.text)
                    csv_write.writerow([
                        line[0][0],
                        line[0][1],
                        line[0][2],
                        getTextPage(urlText)
                    ])
                else:
                    line = re.findall(r"^(.*?), (.*?): (.*)$",day.text)
                    csv_write.writerow([
                        line[0][0],
                        line[0][1],
                        "",
                        line[0][2].replace("; ",";")
                    ])

def getTextPage(url):
    reqText = requests.get(
        'https://lectionary.library.vanderbilt.edu/' + url
    )
    if reqText.status_code != 200:
        return False

    contentText = BeautifulSoup(reqText.text, 'html.parser')
    texts = []
    for text in contentText.select('.texts_msg_bar:nth-of-type(1) ul li a'):
        texts.append(text.text)

    return ";".join(texts)