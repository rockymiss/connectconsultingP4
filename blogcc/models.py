""" Models """

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Posted"))


class BlogPost(models.Model):
    """ Model for Admin to Post a Blog """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogcc_post")
    blog_title = models.CharField(max_length=220, unique=True)
    blog_subtitle = models.TextField(blank=True)
    blog_content = models.TextField()
    blog_created_on = models.DateTimeField(auto_now_add=True)
    blog_updated_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=220, unique=True)
    blog_image_1 = CloudinaryField('image', default='placeholder1')
    blog_image_2 = CloudinaryField('image', default='placeholder2')
    status = models.IntegerField(choices=STATUS, default=0)
    blog_favourite = models.ManyToManyField(
        User,
        related_name='blog_favourite',
        blank=True)

    class Meta:
        """
        blogs are displayed in order from newest to oldest posted
        """
        ordering = ['-blog_created_on']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.blog_title}"

    def number_of_favourites(self):
        """
        Returns total number of times a user has marked
        a blog as a favourite
        """
        return self.blog_favourite.count()


class BlogComment(models.Model):
    """Model for User to leave a comment on a blog"""
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE,
                             related_name="user_comments",)
    name = models.CharField(max_length=70, default="name")
    email = models.EmailField()
    comment_created = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
    approve = models.BooleanField(default=False)

    class Meta:
        """
        comments are ordered from latest to oldest
        """
        ordering = ['comment_created']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.name}, {self.comment_created}"


class Testimonial(models.Model):
    """ Model for Users to Post a Testimonal """
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="testim_user")
    company_name = models.CharField(max_length=220, unique=False)
    content = models.TextField()
    approve = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Testimonals are displayed in order from newest to oldest
        """
        ordering = ['date_created']

    def __str__(self):
        """
        returns string representation of the object
        """
        return f"{self.company_name} wrote {self.content}"
