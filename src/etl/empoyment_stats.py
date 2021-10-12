"""
Group 20: SCOURSE
Members : Abhinaav Singh(abhinaas), Akshay Bahadur(akshayba), Chirag Huria(churia), Naman Arora(namana)
File used for scraping employment history stats that are posted by Henz 

"""

import tabula
import os

# scrape the data inside all the PDFs available at the provided path
def scrape_employment_stats(path):
    for path, subdirs, files in os.walk(path):
        for f in files:
            if f.endswith('.pdf'):
                pdf_path = path + f
                tabula.convert_into(pdf_path, pdf_path.split('.')[0] + ".csv", output_format="csv", pages='all')


if __name__ == '__main__':
    scrape_employment_stats()