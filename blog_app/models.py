from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """Create a new post"""
    title = models.TextField(max_length=70)
    text = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return (f"({self.date_added}) {self.title}: {self.text}\n")