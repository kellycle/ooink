from django.db import models

# Create your models here.
from django.db import models
import re
import datetime
import bcrypt
from datetime import date

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        current_date = datetime.datetime.now()

        if len(postData['first_name']) < 2 and len(postData['last_name']) < 2:
            errors['name'] = "First name & last name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        elif User.objects.filter(email = postData['email']).exists() == True:
            errors['email'] = "Account already exists!"
        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters"
        if postData['password'] != postData['confirm_password']:
            errors['password_check'] = "Your passwords don't match"
        if postData['birthday'] > current_date.strftime("%Y-%m-%d"):
            errors['birthday'] = "Birth date should be past date"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email and/or password"
        elif User.objects.filter(email = postData['email']).exists() != True:
            errors['email'] = "Account does not exist"
        if User.objects.filter(email = postData['email']).exists() == True:
            existing_user = User.objects.filter(email = postData['email']).first()
            if bcrypt.checkpw(postData['password'].encode(), existing_user.password.encode()) != True:
                errors['password'] = "Invalid email and/or password"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateTimeField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    subtotal = models.DecimalField(decimal_places=2, max_digits=6)
    sales_tax = models.DecimalField(decimal_places=2, max_digits=6)
    total_cost = models.DecimalField(decimal_places=2, max_digits=6)
    itemized_order = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
