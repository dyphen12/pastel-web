"""

Tensoreal Games.

application.py

Status: UNDER DEVELOPMENT

Made by Alexis W.

"""

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json
import os

from vibra.api.core import api_version
from vibra.api.users import handler as uhd
from vibra.api.users import charutils as char


app = Flask(__name__)
api = Api(app)
CORS(app)

class Hello(Resource):

    def get(self):
        return api_version()

api.add_resource(Hello, '/')
################# Login Api #######################

CREDENTIAL = {
    'token1':{'user': "admin",
              'pass': "admin1"}
}

CHARDATA = {
    'token1':{'owner': "owner0",
              'charid': "01234",
              'email': "email",
              'cryptos': "0",
              'quantums': "0",
              'hair': "0",
              'torso': "0",
              'pants': "0",
              'shoes': "0",
              'face': "face",
              'head': "head",
              'charname': "charname",
              'level': "0",
              'experience': "0",
              'healthpower': "0",
              'energypower': "0",
              'attackstat': "0",
              'speedstat': "0",
              'defensestat': "0",
              'energystat': "0",
              'bisword': "0",
              'shooter': "0",
              'energy': "0",
              'bard': "0",
              'shieldsword': "0",
              'blockratio': "0",
              'attackrange': "0",
              'posx': "0",
              'posy': "0",
              'posz': "0",
              'jumpforce': "0",
               'runspeed': "0",
              'inventory': "empty",
              'dimensionlocation': "none"}

}

def abort_if_credential_doesnt_exist(token_id):
    if token_id not in CREDENTIAL:
        abort(404, message="Token {} doesn't exist".format(token_id))


parserauth = reqparse.RequestParser()
parserauth.add_argument('user')
parserauth.add_argument('pass')

parserchar = reqparse.RequestParser()
parserchar.add_argument('owner')
parserchar.add_argument('charid')
parserchar.add_argument('email')
parserchar.add_argument('cryptos')
parserchar.add_argument('quantums')
parserchar.add_argument('hair')
parserchar.add_argument('torso')
parserchar.add_argument('pants')
parserchar.add_argument('shoes')
parserchar.add_argument('face')
parserchar.add_argument('head')
parserchar.add_argument('charname')
parserchar.add_argument('level')
parserchar.add_argument('experience')
parserchar.add_argument('healthpower')
parserchar.add_argument('energypower')
parserchar.add_argument('attackstat')
parserchar.add_argument('speedstat')
parserchar.add_argument('defensestat')
parserchar.add_argument('energystat')
parserchar.add_argument('bigsword')
parserchar.add_argument('shooter')
parserchar.add_argument('energy')
parserchar.add_argument('bard')
parserchar.add_argument('shieldsword')
parserchar.add_argument('blockratio')
parserchar.add_argument('attackrange')
parserchar.add_argument('posx')
parserchar.add_argument('posy')
parserchar.add_argument('posz')
parserchar.add_argument('jumpforce')
parserchar.add_argument('runspeed')
parserchar.add_argument('inventory')
parserchar.add_argument('dimensionlocation')



class Login(Resource):

    def post(self):

        args = parserauth.parse_args()
        token_id = int(max(CREDENTIAL.keys()).lstrip('token')) + 1
        token_id = 'token%i' % token_id
        CREDENTIAL[token_id] = {'user': args['user'],
                                'pass': args['pass']}

        token = CREDENTIAL[token_id]

        x, auth = uhd.user_login_ryzen(token['user'],token['pass'])

        if auth is True:
            ids = x[0]['id']
            ssid = ids
            return int(ssid)
        else:
            return x


api.add_resource(Login, '/auth')


class getuserName(Resource):

    def get(self, todo_id):

        x = uhd.get_username_ryzen(int(todo_id))

        return x


api.add_resource(getuserName, '/user/<string:todo_id>')


class SignUp(Resource):

    def get(self, todo_id):
        query = json.loads(todo_id)
        #print(query)
        uusername = query['results']['username']
        uname = query['results']['name']
        ulastname = query['results']['lastname']
        uemail = query['results']['email']
        upass = query['results']['password']
        resulta = uhd.user_signup_ryzen(uusername, uname, ulastname, upass, uemail)

        print(resulta)

        return resulta


api.add_resource(SignUp, '/signup/<string:todo_id>')

# IN-GAME API

class CreateCharacter(Resource):

    def post(self):

        args = parserchar.parse_args()
        token_id = int(max(CREDENTIAL.keys()).lstrip('token')) + 1
        token_id = 'token%i' % token_id
        CHARDATA[token_id] = {'owner': args['owner'],
                                'charid': args['charid'],
                                'email': args['email'],
                                'cryptos': args['cryptos'],
                                'quantums': args['quantums'],
                                'hair': args['hair'],
                                'torso': args['torso'],
                                'pants': args['pants'],
                                'shoes': args['shoes'],
                                'face': args['face'],
                                'head': args['head'],
                                'charname': args['charname'],
                                'level': args['level'],
                                'experience': args['experience'],
                                'healthpower': args['healthpower'],
                                'energypower': args['energypower'],
                                'attackstat': args['attackstat'],
                                'speedstat': args['speedstat'],
                                'defensestat': args['defensestat'],
                                'energystat': args['energystat'],
                                'bigsword': args['bigsword'],
                                'shooter': args['shooter'],
                                'energy': args['energy'],
                                'bard': args['bard'],
                                'shieldsword': args['shieldsword'],
                                'blockratio': args['blockratio'],
                                'attackrange': args['attackrange'],
                                'posx': args['posx'],
                                'posy': args['posy'],
                                'posz': args['posz'],
                                'jumpforce': args['jumpforce'],
                                'runspeed': args['runspeed'],
                                'inventory': args['inventory'],
                                'dimensionlocation': args['dimensionlocation']}

        token = CHARDATA[token_id]



        char.create_char(token)
        #x, auth = uhd.user_login_ryzen(token['user'],token['pass'])


        return 200

api.add_resource(CreateCharacter, '/createchar')

class getCharbyID(Resource):

    def get(self, todo_id):

        x = char.char_by_id(todo_id)

        return x


api.add_resource(getCharbyID, '/char_by_id/<string:todo_id>')


class getCharsbyUser(Resource):

    def get(self, todo_id):

        x = char.get_chars_by_owner(todo_id)

        return x


api.add_resource(getCharsbyUser, '/chars_by_owner/<string:todo_id>')



class getUserCharStamp(Resource):

    def get(self, todo_id):

        x = char.get_char_stamp_for_user(todo_id)

        return x


api.add_resource(getUserCharStamp, '/stamp/<string:todo_id>')

if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    app.run()