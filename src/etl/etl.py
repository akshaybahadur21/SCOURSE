"""
Created on Mon Sep 13 22:15:37 2021

@author: abhinaavsingh
"""
from src.etl.coursicle import scrape_course_list
from src.etl.heinz_courses import scrape_courses_from_heinz


def performETL():
    course_location = scrape_courses_from_heinz()
    scrape_course_list(course_location)


if __name__ == "__main__":
    performETL()
