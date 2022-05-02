"""

Tensoreal Games.

userbase.py

Status: working

Made by Alexis W.

"""

import certifi
import pymongo

ca = certifi.where()

#--------- MONGO DB IMPLEMENTATION -----------------

snkclient = pymongo.MongoClient("mongodb+srv://dimensiondb:dimensionstrife1@usercluster0.msz2u.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)

snkdb=snkclient['gametesters']
snkcoll = snkdb['users']
# Issue the serverStatus command and print the results


def get_user_by_email(email):

    myquery2 = {"email": email}

    resultcursor = list(snkcoll.find(myquery2))

    #print(resultcursor)

    result = resultcursor

    return result

def get_user_by_username(username):

    myquery2 = {"username": username}

    resultcursor = list(snkcoll.find(myquery2))

    result = resultcursor

    return result

def insert_user(userdict):
    x = snkcoll.insert_one(userdict)
    return x

def get_user_by_id(ssid):

    myquery2 = {"id": ssid}

    resultcursor = list(snkcoll.find(myquery2))

    result = resultcursor

    return result

def update_portofolio(ssid, portfolio):
    myquery = {"id": ssid}
    newvalues = {"$set": {"portfolio": str(portfolio)}}

    snkcoll.update_one(myquery, newvalues)

    return True


