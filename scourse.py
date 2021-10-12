"""
Group 20: SCOURSE
Members : Abhinaav Singh(abhinaas), Akshay Bahadur(akshayba), Chirag Huria(churia), Naman Arora(namana)

"""
import argparse

from src.etl.etl import performETL
from src.utils.print_utils import print_banner, print_menu, print_role_menu, print_skillset_menu, str2bool
from src.algo.course_similarity import course_sim

import warnings
warnings.filterwarnings("ignore")


class SCOURSE:
    def __init__(self, perFormETL):
        print_banner()
        self.perFromETL = perFormETL

    def run(self):
        if self.perFromETL:
            performETL()
        while True:
            print_menu()
            choice = input()
            if choice == '2':
                break
            print_role_menu()
            role = input()
            print_skillset_menu()
            skill = input()
            course_sim("{} {}".format(role, skill))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-performETL', "--performETL", help="Perform ETL",
                        type=str2bool, default=False)
    args = parser.parse_args()
    perform_etl = args.performETL
    scourses = SCOURSE(perform_etl)
    scourses.run()
