from django.db import models
from unicentral.apps.core.models import BaseModel
from unicentral.apps.auth_user.models import User


class University(BaseModel):
    name = models.CharField(max_length=150)
    adress = models.CharField(max_length=150)
    province = models.CharField(max_length=100)
    description = models.TextField()

    # d'autre champ peuvent etre necessaire ici


class Cycle(BaseModel):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)


class Faculty(BaseModel):
    university = models.ForeignKey(University, 
                on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, on_delete=models.SET_NULL, null=True)
    faculty_name = models.CharField(max_length=100)

    # d'autre champ peuvent etre necessaire ici


class Departement(BaseModel):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    departement_name = models.CharField(max_length=100)

    # d'autre champ peuvent etre necessaire ici

""" 
Le model nationnality est utiliser pour regrouper 
toutes les nationnalites a partir de la relation avec la candidature,
l'utilisation de TextChoices peut prendre plus des informations dans le code
car beaucoup plus de nationnalites seront inclus

"""

class Nationnality(models.Model):
    name = models.CharField(max_length=100)

class Candidate(BaseModel):
    nationnality = models.ForeignKey(Nationnality, on_delete=models.CASCADE)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    # plusieurs d'autres champs doivent etre inclus ici

class Article(BaseModel):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="image/", blank=True, null=True)
    video = models.FileField(upload_to="video/", blank=True, null=True)
    description = models.TextField()
    author = models.CharField(max_length=100)

    # d'autres champs peuvent etre inclus ici


class Discussion(BaseModel):
    title = models.CharField(max_length=100)
    message = models.TextField()

     # d'autres champs peuvent etre inclus ici


class Response(BaseModel):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)
    response = models.TextField()

    # D'autres champs peuvent etres necessaire ici


