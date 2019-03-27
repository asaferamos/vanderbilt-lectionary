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
        csv_write.writerow([
            'dayweek',
            'day',
            'title',
            'code',
            'first_read',
            'psalm_read',
            'second_read',
            'gospel_read',
            'first_read_comp',
            'psalm_read_comp',
            'second_read_comp',
        ])
        # get weeks
        for dailys in content.select('ul.daily_day'):
            # get days
            for day in dailys.select('li'):
                li = day.find_all('strong')
                # is sunday or special day
                if len(li) > 1:
                    urlText = day.find('a').get('href')

                    line = re.findall(r"^(.*?), (.*?): (.*)$",day.text)
                    textsOtherPage = getTextPage(urlText)
                    lineWrite = [
                        line[0][0],
                        line[0][1],
                        line[0][2]
                    ]

                    lineWrite.extend(textsOtherPage)

                    csv_write.writerow(lineWrite)
                else:
                    dayText = day.text
                    moreText = re.findall(r"(:|;)\s([a-zA-Z]{1,40})\s([0-9:-]{4,50});\s([0-9:-]{4,50})",dayText)
                    if len(moreText) > 0:
                        dayText = dayText.replace(
                            moreText[0][1] + " " + moreText[0][2] + "; " + moreText[0][3],
                            moreText[0][1] + " " + moreText[0][2] + " and " + moreText[0][1] + " " + moreText[0][3]
                        )

                    line = re.findall(r"^(.*?), (.*?): (.*)$",dayText)
                    textsDays = line[0][2].replace(" OR ","; ")
                    textsDays = textsDays.split("; ")
                    lineWrite = [
                        line[0][0],
                        line[0][1],
                        "",
                        "",
                        textsDays[1],
                        textsDays[0],
                        textsDays[2]
                    ]

                    if len(textsDays) == 6:
                        lineWrite.extend([
                            '',
                            textsDays[4],
                            textsDays[3],
                            textsDays[5]
                        ])
                    elif len(textsDays) > 3 or len(textsDays) < 3:
                        print(textsDays)
 
                    csv_write.writerow(lineWrite)

def getTextPage(url):
    reqText = requests.get(
        'https://lectionary.library.vanderbilt.edu/' + url
    )
    if reqText.status_code != 200:
        return False

    contentText = BeautifulSoup(reqText.text, 'html.parser')

    code = contentText.select('.prayers_infobox ul li a')
    code = code[0].get('href').split("LectionaryLink=")

    texts = []
    texts.append(code[1])

    title = contentText.select('#main #sidebar h4')[0]

    if title.text == ' Easter Vigil ':
        easter = contentText.select('.texts_msg_bar:nth-of-type(1) ul')
        texts.append([
            easter[0].text.replace("\n"," ").strip(),
            easter[1].text.replace("\n",""),
            "",
            easter[2].text.replace("\n","")
        ])
    else:
        for text in contentText.select('.texts_msg_bar:nth-of-type(1) ul li'):
            textReplaced = text.text.replace("\xa0\xa0•\xa0","")
            texts.append(textReplaced)

    return texts