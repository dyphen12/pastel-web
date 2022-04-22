"""

Prisma Inc. 2021

unit-testmongo.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from vibra.api.users import handler as hd
from vibra.api.users import userbase as ub




if __name__ == '__main__':
    print(ub.get_user_by_email('alexiswong10@gmail.com'))
    x = [1,2,3,4]
    print(str(x))
