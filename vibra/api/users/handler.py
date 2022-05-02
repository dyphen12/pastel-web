"""

Tensoreal Games.

handler.py

Status: Working

Made by Alexis W.

"""



from vibra.api.users import userbase
import random

#------------------

# Ryzen Connection


def user_login_ryzen(username, password):

    #userobj = userbase.get_user_by_email(email)
    userobj = userbase.get_user_by_username(username)

    if userobj:
        userobjpass = userobj[0]['password']
        if userobjpass == password:
            uname = userobj[0]['username']
            # print('Welcome, {fname}'.format(fname=uname[0]))
            return userobj, True
        else:
            return 'pass', False
    else:
        return 'user', False

def user_signup_ryzen(username, name, lastname, password, email):

    try:
        ids = random.randint(10000, 99999)

        # print(ids)

        userdf = {'id': ids, 'username': username, 'name': name, 'lastname': lastname, 'password': password, 'email': email, 'type': 'player', 'payment': 0, 'quantums': 0}

        # print(userdf)

        usersq = userbase.get_user_by_username(username)
        emailsq = userbase.get_user_by_email(email)

        print(usersq)
        print(type(emailsq))

        if emailsq:
            print("fuc")
            #Email exists
            return '889'


        elif usersq:
            #Username Exists
            return "890"

        else:
            userbase.insert_user(userdf)
            return ids


    except Exception as e:
        #print(e)
        return('Something goes bad')

def get_username_ryzen(ids):

    user = userbase.get_user_by_id(ids)

    print(len(user))

    username = user[0]['username']

    #userobj = user.loc[users['id'] == ids]

    #usersname = userobj['username']

    return username



