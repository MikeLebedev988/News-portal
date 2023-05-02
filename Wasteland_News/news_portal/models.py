from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

article = 'AR'
news = 'NE'

POSTS = [
    (article, 'статья'),
    (news, 'новость'),
]


# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
# Суммарный рейтинг каждой статьи автора умножается на 3.
        a = self.post_set.aggregate(post_rating=Sum('rating'))
        res_sum = 0
        res_sum += a.get('post_rating') * 3
# Суммарный рейтинг всех комментариев автора.
        b = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        res_sum2 = 0
        res_sum2 += b.get('comment_rating')
# Суммарный рейтинг всех комментариев к статьям автора.
        res_sum3 = 0
        count = self.post_set.all().count()
        for i in range(count):
            res_sum3 += self.post_set.all()[i].rating
# Итого:
        self.rating = res_sum + res_sum2 + res_sum3
        self.save()

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    choise = models.CharField(max_length=2, choices=POSTS, default=article)
    date_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=60)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[:123]}..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
