from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum, Max

article = 'AR'
news = 'NE'

POSTS = [
    (article, 'статья'),
    (news, 'новость'),
]


# Create your models here.
def best_author():
    best_author = Author.objects.order_by("-rating")
    print(f'Best Author is {best_author[0].user.username} with {best_author[0].rating} rating points.')

def best_post():
    best_post = Post.objects.order_by("-rating")[0]
    print(f"Best post:"
          f"\nDate_time: {best_post.date_time}"
          f"\nUsername: {best_post.author.user.username}"
          f"\nRating: {best_post.rating}"
          f"\nTitle: {best_post.title}"
          f"\nPreview: {best_post.preview()}"
          f"\n--------------------------")


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        res_sum = res_sum2 = res_sum3 = 0
# Суммарный рейтинг каждой статьи автора умножается на 3.
        a = self.post_set.aggregate(post_rating=Sum('rating'))
        res_sum += a.get('post_rating') * 3
# Суммарный рейтинг всех комментариев автора.
        b = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        res_sum2 += b.get('comment_rating')
# Суммарный рейтинг всех комментариев к статьям автора.
        count_posts = self.post_set.all().count()
        for i in range(count_posts):
            count_comments = self.post_set.all()[i].comment_set.all().count()
            for z in range(count_comments):
                res_sum3 += self.post_set.all()[i].comment_set.all()[z].rating
# Итого:
        self.rating = res_sum + res_sum2 + res_sum3
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)


def all_comments():
    best_post = Post.objects.order_by("-rating")[0]
    comments_count = best_post.comment_set.all().count()
    for i in range(comments_count):
        print(f"Best comment:"
              f"\nDate_time: {best_post.comment_set.all()[i].date_time}"
              f"\nUsername: {best_post.comment_set.all()[i].user}"
              f"\nrating: {best_post.comment_set.all()[i].rating}"
              f"\nComment: {best_post.comment_set.all()[i].text}"
              f"\n-------------------------------------")


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
