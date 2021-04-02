from django.db import models

class User(models.Model):
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    # User.save(prenom,email,password)
    def save(self):
        p = User(prenom,email,password)
        p.save()