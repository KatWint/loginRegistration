from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask
from flask import flash
from flask_bcrypt import Bcrypt
app=Flask(__name__)     
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    db = 'logReg'
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def getAll(cls):
        query = 'SELECT * FROM profile_info;'
        results = connectToMySQL(cls.db).query_db(query)
        allRegistrations = []
        for row in results:
            registration = cls(row)
            allRegistrations.append(registration)
        return allRegistrations

    @classmethod
    def save(cls, data):
        query = 'INSERT INTO user_info (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());'
        return connectToMySQL(cls.db).query_db(query, data)

    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM profiles WHERE email = %(email)s;"
        result = connectToMySQL("mydb").query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_registration(registration):
        is_valid = True 
        if len(registration['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(registration['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(registration['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(registration['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(login):
        is_valid = True 
        if len(login['first_name']) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False
        if len(registration['last_name']) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(registration['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(registration['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid
