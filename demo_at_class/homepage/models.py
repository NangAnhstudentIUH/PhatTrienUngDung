from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.TextField()
    url = models.URLField()
    redirect_url = models.URLField()
    thumb = models.URLField()
    thumb_l = models.URLField()
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.title


from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    website = models.URLField(max_length=255)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    full_name = models.CharField(max_length=255)
    registration_date = models.DateField()
    ROLE_CHOICES = [('admin', 'admin'), ('user', 'user')]
    role = models.CharField(max_length=5, choices=ROLE_CHOICES, default='user')

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField()
    thumb = models.CharField(max_length=255)
    description = models.TextField()

class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

class ArticleTag(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=255)
    comment_content = models.TextField()
    comment_date = models.DateTimeField()