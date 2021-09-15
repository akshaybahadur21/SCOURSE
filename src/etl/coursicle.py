"""
Created on Mon Sep 13 19:45:17 2021

@author: abhinaavsingh
"""

import requests
from bs4 import BeautifulSoup


def scrape_course_list(course_location):
    course_list = []
    with open(course_location) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for l in lines:
            course_list.append(l.split(",")[0])
    listOfCourses = []
    print("Scraping course information for course id's: ", str(course_list), "from coursicle.")
    for course in course_list:
        try:
            course = course.replace("-", "")
            r = requests.get(
                "https://api.scrapingdog.com/scrape?api_key=613ff616b3ce7e6d1135f859&url=http://www.coursicle.com/cmu/courses/ISM/" + str(
                    course) + "/").text
            bsyc = BeautifulSoup(r, "lxml")
            courseMeta = str(bsyc.find('h1').get_text()).split()
            course_id = courseMeta[1]
            courseName = ' '.join(courseMeta[3:])
            professors = []
            professor_tags = bsyc.find_all('a', {"class": "professorLink"})
            for prof in professor_tags:
                professors.append(prof.get_text())
            preDescription = bsyc.find('div', text='Description', attrs={'class': 'subItemLabel'})
            description = preDescription.find_next_sibling("div").get_text()
            preUnits = bsyc.find('div', text='Credits', attrs={'class': 'subItemLabel'})
            units = preUnits.find_next_sibling("div").get_text()
            listOfCourses.append(
                {'courseID': course_id, 'courseName': courseName, 'professors': professors, 'description': description,
                 'units': str(units).strip()})
        except:
            print("Exception")
            pass
    fout = open('resources/data/coursicle_data_dump.txt', 'wt', encoding='utf-8')
    for c in listOfCourses:
        fout.write("%s\n\n" % c)
    fout.close
    print("Coursicle web scraping completed.")
