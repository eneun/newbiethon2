from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    # user = models.ForeignKey(User, related_name='rooms')
    title = models.CharField(max_length=200)
    content = models.TextField()
    GENRES = [('힙합', '힙합'), ('발라드', '발라드'), ('팝송', '팝송'), ('R&B', 'R&B'), ('댄스', '댄스'), ('락', '락')]
    genre = models.CharField(max_length=10, choices=GENRES)
    # genre = models.CharField(max_length=20)
    number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title