from django.db import models
from django.db.models import Avg, Count, Max, Min, Sum


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey('Category', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        ordering = ('-created_at', '-pk')

    def __str__(self):
        return '<Post {}: "{}">'.format(self.pk, self.title[:8])

    @staticmethod
    def get_posts_with_comment():

        qs = Post.objects.annotate(
            comment_count=Count('comment')
        )
        result = qs.filter(comment_count__gte=1)

        return result



class Comment(models.Model):

    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Comment {}: {} - "{}">'.format(self.pk, self.post.title, self.content)


class Tag(models.Model):

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Tag {}: "{}">'.format(self.pk, self.name)


class Category(models.Model):

    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Category {}: "{}">'.format(self.pk, self.name)


