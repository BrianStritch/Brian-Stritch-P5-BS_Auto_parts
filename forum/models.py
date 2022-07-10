""" forum models.py """
# imports
# 3rd party imports from django
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse

STATUS = ((0, 'Draft'), (1, 'Published'))


class ForumCategory(models.Model):
    """ model for ForumCategory table"""

    class Meta:
        """ model to set plural of class name """
        verbose_name_plural = 'Forum Categories'

    name = models.CharField(max_length=254)

    slug = models.SlugField(max_length=200, unique=True)

    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """ returns friendly name """
        return self.friendly_name

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a forum category is created or edited
        """
        return reverse('forum')

    def save(self, *args, **kwargs):
        """
            function to edit and save the slug
            for after a category is created or edited
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ForumTopics(models.Model):
    """ model for forumtopics """

    class Meta:
        """ class to set plural of class name"""
        verbose_name_plural = 'Forum Topics'

    forum_category = models.ForeignKey(ForumCategory, on_delete=models.CASCADE)

    name = models.CharField(max_length=254)

    slug = models.SlugField(max_length=200, unique=True)

    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    summary = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a forum topic is created or edited
        """
        return reverse('forum')

    def save(self, *args, **kwargs):
        """
            function to edit and save the slug
            for after a topic is created or edited
        """
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_friendly_name(self):
        """ returns friendly name """
        return self.friendly_name


class ForumPost(models.Model):
    """ model for forumpost """

    title = models.CharField(max_length=199)

    slug = models.SlugField(max_length=200)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    topic = models.ForeignKey(ForumTopics,
                              null=True,
                              blank=True,
                              on_delete=models.CASCADE)

    updated_on = models.DateTimeField(auto_now=True)

    content = models.TextField()

    summary = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    status = models.IntegerField(choices=STATUS, default=0)

    likes = models.ManyToManyField(User,
                                   related_name='forum_post_likes',
                                   blank=True)

    class Meta:
        """ sets the plural for classname """
        ordering = ['-created_on']
        verbose_name_plural = 'Forum Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
            function to define the reverse URL
            for after a forum post is created or edited
        """
        return reverse('forum')

    def save(self, *args, **kwargs):
        """
            function to edit and save the slug
            for after a post is created or edited
        """
        self.slug = slugify(self.title, )
        super().save(*args, **kwargs)

    def number_of_likes(self):
        """ reurns the total number of likes"""
        return self.likes.count()

    def number_of_posts(self):
        """ returns the total number of posts """
        return self.title.count()


class ForumPostComment(models.Model):
    """ model for forum post comment """

    post = models.ForeignKey(ForumPost,
                             on_delete=models.CASCADE,
                             related_name='forum_post_comments')

    name = models.CharField(max_length=80)

    email = models.EmailField()

    body = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)

    likes = models.ManyToManyField(User,
                                   related_name='forum_comment_likes',
                                   blank=True)

    class Meta:
        """sets the ordering method """
        ordering = ['created_on']
        verbose_name_plural = 'Forum Post comments'

    def number_of_likes(self):
        """
        function to return the total number of likes
        on a forum post comment
        """
        return self.likes.count()

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
