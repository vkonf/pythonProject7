from datetime import datetime
from django.contrib.auth.models import User


from django.db import models
from django.db.models import Avg, Count, Min, Sum


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        rating_post_author = self.post_set.all().aggregate(Sum('rating_post'))['rating_post__sum'] * 3

        rating_comment_author = self.user.comment_set.all().aggregate(Sum('rating_comment'))['rating_comment__sum']

        rating_comment_post = self.post_set.all().aggregate(Sum('comment__rating_comment'))['comment__rating_comment__sum']

        self.rating_author=rating_post_author+rating_comment_author+rating_comment_post

        self.save()



        return self.rating_author

        # rating_post_author = self.post_set.all()


class Category(models.Model):
    name_category = models.CharField(max_length=30, unique=True)

class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    header = models.CharField(max_length=30)
    content = models.TextField()
    rating_post = models.IntegerField(default=0)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", through='PostCategory')
    genre = models.CharField(max_length=2, choices=[('СТ', 'статья'), ('Но', 'новость')], default='СТ')

    def like(self):
        like_post = self.rating_post
        like_post += 1
        self.rating_post = like_post
        self.save()

    def dislike(self):
        dislike_post = self.rating_post
        dislike_post -= 1
        if dislike_post >=0:
            self.rating_post = dislike_post
        else: self.rating_post=0
        self.save()

    def preview(self):
        s=self.content
        return s[0:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=300)
    time_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    def like(self):
        like_comment = self.rating_comment
        like_comment += 1
        self.rating_comment = like_comment
        self.save()

    def dislike(self):
        dislike_comment = self.rating_comment
        dislike_comment -= 1
        if dislike_comment >=0:
            self.rating_comment = dislike_comment
        else: self.rating_comment=0
        self.save()



