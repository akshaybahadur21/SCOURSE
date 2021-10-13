"""
Group 20: SCOURSE
Members : Abhinaav Singh(abhinaas), Akshay Bahadur(akshayba), Chirag Huria(churia), Naman Arora(namana)

"""

import warnings

from src.algo.course_similarity import course_sim
from src.etl.etl import performETL
from src.utils.print_utils import print_banner, print_menu, print_role_menu, print_skillset_menu

warnings.filterwarnings("ignore")


class SCOURSE:
    def __init__(self):
        print_banner()

    def run(self):
        while True:
            print_menu()
            choice = input()
            if choice == '3':
                break
            elif choice == '2':
                performETL()
            elif choice == '1':
                print_role_menu()
                role = input()
                print_skillset_menu()
                skill = input()
                try:
                    course_sim("{} {}".format(role, skill))
                except:
                    print("Couldn't process the query. Try again")
                    pass
            else:
                print("Please select an appropriate input.")


if __name__ == '__main__':
    scourses = SCOURSE()
    scourses.run()
