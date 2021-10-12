"""
Group 20: SCOURSE
Members : Abhinaav Singh(abhinaas), Akshay Bahadur(akshayba), Chirag Huria(churia), Naman Arora(namana)

"""
import argparse


def print_banner():
    print("""
   _____  _____ ____  _    _ _____   _____ ______ 
  / ____|/ ____/ __ \| |  | |  __ \ / ____|  ____|
 | (___ | |   | |  | | |  | | |__) | (___ | |__   
  \___ \| |   | |  | | |  | |  _  / \___ \|  __|  
  ____) | |___| |__| | |__| | | \ \ ____) | |____ 
 |_____/ \_____\____/ \____/|_|  \_\_____/|______|
                                                  
    """)


def print_menu():
    print("""
    1. Perform Search
    2. Exit
    """)


def print_role_menu():
    print("""
    Enter your desired role
    """)


def print_skillset_menu():
    print("""
    Enter your desired skillset
    """)


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
