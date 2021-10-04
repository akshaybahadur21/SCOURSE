import tabula
import os


def scrape_employment_stats(path):
    for path, subdirs, files in os.walk(path):
        for f in files:
            if f.endswith('.pdf'):
                pdf_path = path + f
                tabula.convert_into(pdf_path, pdf_path.split('.')[0] + ".csv", output_format="csv", pages='all')


if __name__ == '__main__':
    scrape_employment_stats()