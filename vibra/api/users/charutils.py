# Made by @dyphen12

"""

Tensoreal Games.

userbase.py

Status: UNDER DEVELOPMENT for Character Database

Made by Alexis W.

"""

import certifi
import pymongo
import random
from vibra.api.users import userbase as udb

ca = certifi.where()

#--------- MONGO DB IMPLEMENTATION -----------------

snkclient = pymongo.MongoClient("mongodb+srv://dimensiondb:dimensionstrife1@usercluster0.msz2u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

snkdb=snkclient['gametesters']
snkcoll = snkdb['characters']
# Issue the serverStatus command and print the results


def get_char_by_email(email):

    myquery2 = {"email": email}

    resultcursor = list(snkcoll.find(myquery2))

    result = resultcursor

    return result

def get_chars_by_owner(owner):

    myquery2 = {"owner": owner}

    resultcursor = list(snkcoll.find(myquery2))

    result = resultcursor

    print(result)

    characters = []

    for char in result:
        #char.pop("_id")
        characters.append(char["charid"])

    print(characters)

    if len(characters) == 0:
        return "empty"

    return characters

def insert_char(userdict):
    x = snkcoll.insert_one(userdict)
    return x


def char_by_id(ssid):

    myquery2 = {"charid": ssid}

    resultcursor = list(snkcoll.find(myquery2))

    print(resultcursor)

    print(type(resultcursor[0]))

    resultcursor[0].pop("_id")

    return resultcursor[0]

def update_char(ssid, portfolio):
    """
    Update Character.

    Args:
        ssid: This is the first param.
        portfolio: This is a second param.

    Returns:
        bool

    Raises:
        KeyError: Raises an exception.
    """
    myquery = {"id": ssid}
    newvalues = {"$set": {"portfolio": str(portfolio)}}

    snkcoll.update_one(myquery, newvalues)

    return True


def create_char(chartoken):

    try:

        print(chartoken)
        print(type(chartoken))

        # print(ids)

        #userdf = {'id': ids,'username': username,'name': name,'lastname': lastname,'password': password,'email': email,'type': 'citizen','payment': 0}

        insert_char(chartoken)


    except Exception as e:
        #print(e)
        return('Something goes bad')



def check_char_id(ids):

    myquery2 = {"charid": ids}

    resultcursor = list(snkcoll.find(myquery2))

    return resultcursor



def get_char_by_id(ids):

    chars = char_by_id(ids)

    charobj = chars.loc[chars['charid'] == ids]

    chardata = charobj.to_dict()

    print(chardata)

    chardata.pop("_id")

    return chardata

def get_char_stamp_for_user(username):

    user = udb.get_user_by_username(username)

    user[0].pop("_id")

    finded = False

    while finded is False:
        ids = random.randint(100000, 999999)
        test2 = check_char_id(ids)
        if test2:
            print("char id exist")
            finded = False
        else:
            finded = True
            charid = ids

    print(user)

    userstamp = {'charid': charid, 'username': username, 'email': user[0]['email']}

    print(userstamp)

    return userstamp

