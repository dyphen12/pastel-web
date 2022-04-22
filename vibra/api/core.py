"""

Prisma Inc. 2022

core.py

Status: Checked

Note: The core of the API.

Made by Alexis W.

"""
import json

# Connections to RapidAPI
# Works as the API core, the Sneakers Data.
# Use this methods to Update and Set-up the API data.

class Config:
    def __init__(self, dbs, imglit, apik, inys, localimg, airkey, airbasekey):
        self.dbsize = dbs
        self.imglitter = imglit
        self.apikey = apik
        self.inysize = inys
        self.localimg = localimg
        self.airkey = airkey
        self.airbasekey = airbasekey


def load_config():
    config_loc = 'vibra/config.json'
    try:
        with open(config_loc) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()

        dbsize = jsonObject['api-config']['db-size']
        imagelitter = jsonObject['api-config']['image-row-litter']
        apikey = jsonObject['api-config']['api-key']
        inysize = jsonObject['api-config']['iny-base-size']
        localimg = jsonObject['api-config']['local-imaging']
        airkey = jsonObject['api-config']['air-key']
        airbasekey = jsonObject['api-config']['airbase-key']

        cf = Config(dbsize, imagelitter, apikey, inysize, localimg, airkey, airbasekey)

        return cf

    except FileNotFoundError:
        print('Config not found.')


def api_version():
    version = '0.0.1'
    return version