# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class usersManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        # check DB for post_data['email']
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

    # def books_reviewed(self):
    #     return self.model.reviews_left.all().values('book').distict()

    def validate_registration(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['name']) < 2:
            errors.append("Name fields must be at least 3 characters")
        # check length of name password
        if len(post_data['password']) < 8:
            errors.append("Password must be at least 8 characters")
        # check name fields for letter characters
        if not re.match(NAME_REGEX, post_data['name']):
            errors.append('Name fields must be letters only')
        # check emailness of email
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Invalid email")
        # check uniqueness of email
        if len(users.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email already in use")
        # check password == password_confirm
        if post_data['password'] != post_data['password_confirm']:
            errors.append("Passwords do not match")

        if not errors:
            # make our new user
            # hash password
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                name=post_data['name'],
                email=post_data['email'],
                password=hashed
            )
            return new_user
        return errors


class users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    objects = usersManager()
    def __str__(self):
        return self.email
