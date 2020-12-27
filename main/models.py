from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post (models.Model):
    movie_name = models.CharField(max_length = 100)
    review = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    # creatinf absolute method
    # so that it can revese the url as a string
    
    def get_absolute_url(self):
        return reverse('detailpage', kwargs={'pk' : self.pk})

    def __str__(self):
        return self.movie_name
# dunder class overloading so that we can see the contains of objects in query
# in this case we can see the movie name

