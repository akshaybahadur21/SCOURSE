import re

import requests
from bs4 import BeautifulSoup


def striphtml(data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', str(data))
    return cleantext


def scrape_courses_from_heinz():
    listOfCourses = []
    r = requests.get("https://api.heinz.cmu.edu/courses_api/course_list/").text
    bsyc = BeautifulSoup(r, "lxml")
    table = bsyc.find_all("div", {"class": "col-12"})
    table = table[2]
    rows = table.findAll('tr')
    count = 0
    for r in rows:
        count += 1
        if count == 1:
            continue
        course = r.findAll('td')
        temp_list = [striphtml(course[0]), striphtml(course[1]), striphtml(course[2])]
        listOfCourses.append(temp_list)
    fout = open('resources/data/heinz_courses.txt', 'wt', encoding='utf-8')
    for c in listOfCourses:
        fout.write("%s\n" % ','.join(c))
    fout.close
    return 'resources/data/heinz_courses.txt'


if __name__ == '__main__':
    scrape_courses_from_heinz()
