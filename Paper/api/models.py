from django.db import models
from datetime import datetime

class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)


    def __str__(self) -> str:
        return self.locationName
    
class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_add = models.DateTimeField(auto_now_add=True)

    itemLocation = models.ForeignKey(
        to=Location,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.itemName
    

class User(models.Model):
    user_id = models.AutoField(primary_key=True, unique=True, editable=False, auto_created=True, serialize=True)

    username = models.CharField(max_length=100, unique=True)
    hassed_password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    birthday = models.DateField()

    date_register = models.DateTimeField(default=datetime.now)
    last_login = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.username
    

class Role(models.Model):
    role_id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    role_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.role_name

class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self) -> str:
        return f'{self.role.role_name:15} - {self.user.username}'
    
class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    permission_name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.permission_name
    
class PermissionRole(models.Model):
    permission_role_id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    permission = models.ForeignKey(
        to=Permission,
        on_delete=models.CASCADE,
    )

    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('permission', 'role')
    

class PasswordReset(models.Model):
    token_id = models.AutoField(primary_key=True, auto_created=True, serialize=True)
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    token = models.CharField(max_length=100)
    expired = models.DateTimeField()

    def __str__(self) -> str:
        return self.token
    
class TwoFactorAuthentication(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    method = models.CharField(max_length=100)
    verification_code = models.CharField(max_length=100)
    expired = models.DateTimeField()

    def __str__(self) -> str:
        return self.method



class Article(models.Model):
    id = models.TextField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.TextField()
    thumb = models.URLField()
    thumbL = models.URLField()
    publisher = models.CharField(max_length=255)
    publishedDate = models.DateTimeField()
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.title  


class Tag(models.Model):
    name = models.CharField(max_length=100)
    istop = models.BooleanField(default=False)
    article = models.ForeignKey(Article, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return self.name if not self.istop else f'**{self.name.upper()}'