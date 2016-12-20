from django.conf import settings
from django.db import models

# Create your models here.

User = settings.AUTH_USER_MODEL # 'auth.User'


class Car(models.Model):
    #user    = models.ForeignKey(User) 
    drivers = models.ManyToManyField(User)
    name    = models.CharField(max_length=120)

    def __str__(self): # __unicode__
        return self.name



# car_1 = Car.objects.first()
# user_qs = car_1.drivers.all()  # returns queryset of users

# cfe = user_qs.first()
# cfe.car_set.all()


# Car.objects.filter(drivers=cfe)

# Car.objects.filter(drivers__in= user_qs )









# ForeignKey = ManyToOneField() #Many Users can have any car, car can only have 1 user

# car_obj = Car.objects.first()
# car_obj.user

# User = car_obj.user.__class__

# abc = User.objects.all().last() # filter querysets

# user_cars = abc.car_set.all() 

# user_cars_qs = Car.objects.filter(user=abc)


# class Comment(models.Model):
#     user    = models.ForeignKey(User) 
#     content = models.CharField(max_length=120)


# comments = abc.comment_set.all()
# comments_qs = Comment.objects.filter(user=abc)




