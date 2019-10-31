from django.db import models
from django.conf import settings
from django.utils import timezone


class Rev(models.Model):  # class indicates we are defining an object, model.Models means object is a Django model
    title = models.CharField(max_length=200)  # fields
    author = models.CharField(max_length=200)
    price = models.FloatField()
    GENRE_CHOICE = (
        ('Sci-FI', 'Sci-Fi'),
        ('Mystery', 'Mystery'),
        ('Children', 'Children'),
        ('Horror', 'Horror'),
        ('Political Thriller', 'Political Thriller'),
        ('Self-Help', 'Self-Help'),
        ('Biography', 'Biography'),
        ('Textbook', 'Textbook'),
        ('Picture Book', 'Picture Book'),
        ('Travel', 'Travel'),
    )
    genre = models.CharField(max_length=50, choices=GENRE_CHOICE, null=True)
    AGE_CHOICE = (
        ('Toddler', 'Toddlers'),
        ('Kids', 'Kids'),
        ('Young Adult', 'Young Adult'),
        ('College', 'College'),
        ('Adults', 'Adults'),
    )
    age = models.CharField(max_length=50, choices=AGE_CHOICE, null=True)
    review = models.TextField(max_length=2000)

    def __str__(self):
        return self.title





# python manage.py makemigrations review
# python manage.py migrate review

