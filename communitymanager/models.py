from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Communaute(models.Model):
    nom = models.CharField(max_length=100)
    abonnes = models.ManyToManyField(User, through='abonnements', related_name='+')

class abonnements(models.Model) :
    abonne = models.ForeignKey(User, on_delete=models.CASCADE)
    Commu = models.ForeignKey(Communaute, on_delete=models.CASCADE)

class Priorite(models.Model):
    label = models.CharField(max_length=100)

class Post(models.Model):
    description = models.TextField(null=True)
    date = models.DateTimeField(default=timezone.now)
    communaute = models.ForeignKey('Communaute', on_delete=models.CASCADE)
    auteur = models.ForeignKey('User', on_delete=models.CASCADE)
    priorite = models.ForeignKey('Priorite', on_delete=models.CASCADE)
    evenementiel = models.BooleanField(null=True)
    date_evenement = models.DateTimeField(null=True)

class Commentaire(models.Model):
    date_creation = date = models.DateTimeField(default=timezone.now)
    contenu = models.TextField
    auteur = models.ForeignKey('User', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
