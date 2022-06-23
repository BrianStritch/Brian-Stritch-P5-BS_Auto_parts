from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse


STATUS = ((0, 'Draft'), (1, 'Published'))


class ForumCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Forum Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ForumTopics(models.Model):

    class Meta:
        verbose_name_plural = 'Forum Topics'

    forum_category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ForumPost(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    topic = models.ForeignKey(ForumTopics, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='forum_post_likes', blank=True)

    
    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = 'Forum Posts'  

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class ForumPostComment(models.Model):
    
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='forum_post_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Forum Post comments'

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

