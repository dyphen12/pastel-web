"""

Prisma Inc.

handler.py

Status: UNDER DEVELOPMENT for Major Update Ryzen

Made by Alexis W.

"""



from vibra.api.users import userbase
import random

#------------------

# Ryzen Connection


def user_login_ryzen(email, password):

    userobj = userbase.get_user_by_email(email)

    exist = len(userobj)

    if exist != 0:
        userobjpass = userobj['password'].values
        if userobjpass == password:
            uname = userobj['name'].values
            # print('Welcome, {fname}'.format(fname=uname[0]))
            return userobj, True
        else:
            return 'Wrong Password', False

    else:
        return 'User does not exist', False

def user_signup_ryzen(name, lastname, password, email):

    try:
        ids = random.randint(10000, 99999)

        # print(ids)

        userdf = {'id': ids, 'name': name, 'lastname': lastname, 'password': password, 'email': email, 'type': 'citizen', 'payment': 0}

        # print(userdf)

        emailsq = userbase.get_user_by_email(email)

        if emailsq.empty:

            #print('jue')

            userbase.insert_user(userdf)

            return ids

        else:
            return 'User Already Registered'

    except Exception as e:
        #print(e)
        return('Something goes bad')

def get_username_ryzen(ids):

    users = userbase.get_user_by_id(ids)

    userobj = users.loc[users['id'] == ids]

    usersname = userobj['name']

    return usersname



