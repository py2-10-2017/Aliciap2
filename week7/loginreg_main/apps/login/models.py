# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from django.db import models
import bcrypt

# Create your models here.

EMAIL_MATCH = re.compile(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')

class UserManager(models.Manager):

    def validate_registration(self, post_data):
        errors = []
        
        # Check all fields for any input
        # loop through entire dictionary look for a single empty field
        for key, value in post_data.iteritems():
            if len(value) < 1:
                errors.append("All fields are reqired")
                break
        

        # Minimum length on names
        if len(post_data['first_name']) < 3 or len(post_data['last_name']) < 3:
            errors.append("Name fields must be at least 3 characters")


        # Valid email
        if not re.match(EMAIL_MATCH, post_data['email']):
            errors.append("Email not valid")

        # passwords match
        if post_data['password'] != post_data['password_confirm']:
            errors.append("Passwords do not match")

        # If there is an Existing email
        # this will return [] if no match is found
        if self.filter(email=post_data['email']):
            errors.append("This email is already in use.")

        if not errors:
            hashed_pw = bcrypt.hashpw(post_data['password'].encode(), bcrypt.gensalt())

            self.create(
                first_name = post_data['first_name'],
                last_name = post_data['last_name'],
                email = post_data['email'],
                password = hashed_pw
            )

        return errors
        
      


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)

    objects = UserManager()
 
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)