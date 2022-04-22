# Made by @dyphen12

from flask import Flask, request
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import json
import os

from vibra.api.core import api_version
from vibra.api.users import handler as uhd


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

def abort_if_credential_doesnt_exist(token_id):
    if token_id not in CREDENTIAL:
        abort(404, message="Token {} doesn't exist".format(token_id))


parserauth = reqparse.RequestParser()
parserauth.add_argument('user')
parserauth.add_argument('pass')


class Login(Resource):

    def post(self):

        args = parserauth.parse_args()
        token_id = int(max(CREDENTIAL.keys()).lstrip('token')) + 1
        token_id = 'token%i' % token_id
        CREDENTIAL[token_id] = {'user': args['user'],
                                'pass': args['pass']}

        token = CREDENTIAL[token_id]

        x, auth = uhd.user_login_ryzen(token['user'],token['pass'])

        try:

            ids = x['id'].values[0]



            ssid = ids
            #print('auth success')

            return int(ssid)


        except TypeError:
            ids = 0
            print('auth failed')
            return 'fail'


api.add_resource(Login, '/auth')


class getuserName(Resource):

    def get(self, todo_id):

        x = uhd.get_username_ryzen(int(todo_id))

        return x.values[0]


api.add_resource(getuserName, '/user/<string:todo_id>')


class SignUp(Resource):

    def get(self, todo_id):
        query = json.loads(todo_id)
        uname = query['results']['name']
        ulastname = query['results']['lastname']
        uemail = query['results']['email']
        upass = query['results']['password']
        resulta = uhd.user_signup_ryzen(uname, ulastname, upass, uemail)

        return resulta


api.add_resource(SignUp, '/signup/<string:todo_id>')


if __name__ == '__main__':
#    #app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
    app.run()