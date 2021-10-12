"""
Group 20: SCOURSE
Members : Abhinaav Singh(abhinaas), Akshay Bahadur(akshayba), Chirag Huria(churia), Naman Arora(namana)
This is the master script that calls methods from other scripts to prepare the datasets for performing the analysis.

"""

#importing dependencies
from src.etl.coursicle import scrape_course_list
from src.etl.heinz_courses import scrape_courses_from_heinz
from src.etl.empoyment_stats import scrape_employment_stats
import pandas as pd
import re


def performETL():
    print("Performing ETL operations")
    course_location = scrape_courses_from_heinz() #scrape heinz course catalog
    scrape_course_list(course_location) #scrape course description from coursicle for the courses found in course catalog
    scrape_employment_stats('resources/data/') #scrape employment stats and course to career mapping from PDFs

    coursicle_df = pd.read_csv('resources/data/coursicle_data.csv', error_bad_lines=False,
                               names=["course_id", "course_name", "course_desc", "units"])
    heinz_df = pd.read_csv('resources/data/heinz_courses.csv', error_bad_lines=False,
                           names=["course_id", "course_name", "units"])
    smart_df = pd.read_csv('resources/data/Project Prototype Data - SmartEval_clean.csv', error_bad_lines=False)
    heinz_df['course_id'] = [re.sub(r'\-', '', str(x)) for x in heinz_df['course_id']]
    # coursicle_df['course_id'] = [re.sub(r'(\w+\s\w+)', '', str(x)) for x in coursicle_df['course_id']]
    coursicle_df['course_id'] = coursicle_df['course_id'].astype(int)
    heinz_df['course_id'] = heinz_df['course_id'].astype(int)

    master = pd.merge(coursicle_df, heinz_df, on='course_id')
    smart_df.rename(columns={'Num': 'course_id'}, inplace=True)
    master = pd.merge(master, smart_df, on='course_id')

    master.to_csv('master_data.csv', index=False, sep=',', encoding='utf-8') #write master data to file


if __name__ == "__main__":
    performETL()
