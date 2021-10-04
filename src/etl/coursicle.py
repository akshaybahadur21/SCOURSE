"""
Created on Mon Sep 13 19:45:17 2021

@author: abhinaavsingh
"""

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


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
            
            #For most courses, the url has the ISM path
            try:
                req = requests.get(
                "https://api.scrapingdog.com/scrape?api_key=6143dd1d632a6c4dc0f276c0&url=http://www.coursicle.com/cmu/courses/ISM/" + str(
                    course) + "/")
                r = req.text
            except: # HTTPError as http_error:
                print("Exception raised: ", req.status_code)
            
            
            bsyc = BeautifulSoup(r, "lxml")
            
            #In case the url has HC path. For general heinz courses
            if bsyc.find('title').get_text() == "404 Not Found":
                r = requests.get(
                "https://api.scrapingdog.com/scrape?api_key=6143dd1d632a6c4dc0f276c0&url=http://www.coursicle.com/cmu/courses/HC/" + str(
                    course) + "/").text
                bsyc = BeautifulSoup(r, "lxml")
                
            #For the remaining Public Policy classes. The url here is under PPP
            if bsyc.find('title').get_text() == "404 Not Found":
                url_string = "https://api.scrapingdog.com/scrape?api_key=6143dd1d632a6c4dc0f276c0&url=http://www.coursicle.com/cmu/courses/PPP/" + str(
                    course) + "/"
                r = requests.get(url_string).text
                bsyc = BeautifulSoup(r, "lxml")
           
            
            #Getting the values for fields for each course
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
            
            #Appending to the course list
            listOfCourses.append(
                {'courseID': course_id, 'courseName': str(courseName).replace(",",";"), 'professors': str(professors).replace(",",";"), 'description': str(description).replace(",",";"),
                 'units': str(units).strip()})
            print("Course", course_id, "added.")
        except:
            print("Exception raised. ")
            pass
    
    #Storing it in the dump file
    fout = open('resources/data/coursicle_data_dump.txt', 'wt', encoding='utf-8')
    for c in listOfCourses:
        dict_values = str(dict(c).values()).strip("dict_values")
        fout.write("%s\n" % dict_values)
    fout.close
    print("Coursicle web scraping completed.")