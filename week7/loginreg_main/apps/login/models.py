# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.

EMAIL_PATTERN = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class FriendManager(models.Manager):

    def validate_login(self, post_data):
        """
        check post request for valid data
        if valid returns tuple ([], <Friend Object>)
        if not returns ([error list], None)
        """
        errors = []
        user = None

        # email exists in DB
        if not self.filter(email = post_data['email']):
            errors.append('Invalid email/password')
        
        else:
            # correct pw on user in DB
            user = self.get(email=post_data['email'])
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('Invalid email/password')
            
        return errors, user

    def validate_registration(self, post_data):
        """
        checks post request for valid data,
        if valid returns tuple ([], <Friend Object>)
        if not returns ([error list], None)
        """
        errors = []
        user = None
        # all fields are required
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors.append("All fields are required")
                break

        # min length on name fields (3)
        if len(post_data['first_name']) < 2 or len(post_data['last_name']) < 2:
            errors.append("Name fields must be 2 or more")

        # min length on password
        if len(post_data['password']) < 8:
            errors.append("Password  must be 8 or more characters")

        # passwords match
        if post_data['password'] != post_data['password_confirm']:
            errors.append("password does not match")

        # email is a valid email
        if not re.match(EMAIL_PATTERN, post_data['email']):
            errors.append("invalid email")
        
        # email is in use
        if self.filter(email=post_data['email']):
            errors.append("email in use")

        if post_data['first_name'] == "Devon":
            errors.append("Devons not allowed")
        
        # create user if no errors
        if not errors:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())

            user = self.create(
                first_name = post_data['first_name'],
                last_name = post_data['last_name'],
                email = post_data['email'],
                password = hashed_pw
            )            
        return errors, user


class Friend(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)

    objects = FriendManager()
 
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Note(models.Model):
    message = models.TextField(max_length=100)
    author = models.ForeignKey(Friend, related_name="notes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Note left by Friend #{}".format(self.author.first_name)
