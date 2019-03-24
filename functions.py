# coding: utf-8
import requests, re, csv
from bs4 import BeautifulSoup


def getDailyByYear(year) :
    req = requests.get('https://lectionary.library.vanderbilt.edu/daily.php?year=' + year)
    if req.status_code != 200:
        return False

    content = BeautifulSoup(req.text, 'html.parser')

    with open('data.csv', mode='w') as csv_file:
        csv_write = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # get weeks
        for dailys in content.select('ul.daily_day'):
            # get days
            for day in dailys.select('li'):
                li = day.find_all('strong')
                # is sunday or special day
                if len(li) > 1:
                    urlText = day.find('a').get('href')
                else:
                    line = re.findall(r"^(.*?), (.*?): (.*)$",day.text)
                    csv_write.writerow(line[0])
                    print(line[0][0])