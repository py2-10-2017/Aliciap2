# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import Users
from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, related_name="books")
    def __str__(self):
        return self.title

class ReviewManager(models.Manager):
    def validate_review(self, post_data):
        errors = []

        if len(post_data['title']) < 1 or len(post_data['review']) < 1:
            errors.append('fields are required')
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')

        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')
        if not int(post_data['rating']) > 0 or not int(post_data['rating']) <= 5:
            errors.append('invalid rating')
        return errors

    def create_review(self, clean_data, user_id):
        # create author
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Authors.objects.get(id=int(clean_data['author']))
        else:
            the_author = Authors.objects.create(name=clean_data['new_author'])
        # create a book
        the_book = None
        if not Books.objects.filter(title=clean_data['title']):
            the_book = Books.objects.create(
                title=clean_data['title'], author=the_author
            )
        else:
            the_book = Books.objects.get(title=clean_data['title'])
        # returns a Review object
        return self.create(
            review = clean_data['review'],
            rating = clean_data['rating'],
            book = the_book,
            reviewer = Users.objects.get(id=user_id)
        )

    def recent_and_not(self):

        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Reviews(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Books, related_name="reviews")
    reviewer = models.ForeignKey(Users, related_name="reviews_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ReviewManager()
    def __str__(self):
        return "Books: {}".format(self.book.title)
