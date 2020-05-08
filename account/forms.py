from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password, check_password
from account.models import Account
#from urllib.request import urlopen
#from random import randint

import json, re

class Ajax(forms.Form):

    args = []
    #user = []

    def __init__(self, *args, **kwargs):
        self.errordict = {
        'usernameerror': '',
        'emailerror': '',
        'passworderror': '',
        'Status':'Error'
        }
        self.args = args
        # if len(args) > 1:
        #     self.user = args[1]
        #     if self.user.id == None:
        #         self.user = "NL"

    def error(self):
        return self.errordict
        #return json.dumps({ "Status": "Error","Message": message,"name":name }, ensure_ascii=False)

    def success(self, message):
        return { "Status": "Success", "Message": message }

    # def items(self, json):
    #     return json

    # def output(self):
    #     return self.validate()

class AjaxSignUp(Ajax):

    def validate(self):
        try:
            self.username = self.args[0]["username"]
            self.password = self.args[0]["password"]
            self.email = self.args[0]["email"]
        except Exception as e:
        	return json.dumps({'Status':'Error','Message':'Account Creation Failed'})


        if not re.match('^[a-zA-Z0-9_]+$', self.username):
            self.errordict['usernameerror'] = 'Username must be an alphanumeric character'
        elif Account.objects.filter(username=self.username).exists():
            self.errordict['usernameerror'] = 'Username already exists'

        if not re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            self.errordict['emailerror'] = 'Invalid Email format'
        elif Account.objects.filter(email=self.email).exists():
            self.errordict['emailerror'] = 'Email already registered'
        
        if len(self.password) < 6:
            self.errordict['passworderror'] = 'Password must be of atleast 6 characters'
        elif not re.match('^.*[0-9]+.*$', self.password):
            self.errordict['passworderror'] = 'Password must contain a numeric character'
        elif not re.match('^.*[a-zA-Z]+.*$', self.password):
            self.errordict['passworderror'] = 'Password must contain an alphabetic character'

        if self.errordict['usernameerror']==self.errordict['passworderror']==self.errordict['emailerror']=='':
            u = Account(username=self.username, password=make_password(self.password), email=self.email)
            u.save()
            return self.success("Account Created!")

        return self.error()


class AjaxLogin(Ajax):

    def validate(self):
        try:
            self.password = self.args[0]["password"]
            self.email = self.args[0]["email"]
        except Exception as e:
        	return json.dumps({'Status':'Error','Message':'Account Creation Failed'})

            
        if not Account.objects.filter(email=self.email).exists():
            return False, {'Status':'Error', 'Message':'Incorrect Email or Password'}
        elif not check_password(self.password, Account.objects.get(email=self.email).password):
            return False, {'Status':'Error', 'Message':'Incorrect Email or Password'}

        u = Account.objects.get(email=self.email)

        return u, {'Status':'Success', 'Message':'User Logged In'}
