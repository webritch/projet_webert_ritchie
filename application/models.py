from django.db import models
# Create your models here.

class Cours(models.Model):
    nom_cours = models.CharField(max_length=20)
    ressources = models.CharField(max_length=20)
    credits = models.CharField(max_length=20)

class Programme(models.Model):
    domaine = models.CharField(max_length=20)
    mention = models.CharField(max_length=20)
    specialite = models.CharField(max_length=20)
    langue = models.CharField(max_length=10)
    niveau = models.CharField(max_length=20)

class Prof(models.Model):
    nom_prof = models.CharField(max_length=20)
    prenom_prof = models.CharField(max_length=20)
    profession = models.CharField(max_length=20)
    matiere_enseignee = models.CharField(max_length=20)
    user = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    #tel_prof = models.IntField(max_lenght=15)

    def __unicode__(self):
        return self.user

class Plan_cours(models.Model):
    objectif = models.TextField(null = True)
    type_evaluation = models.CharField(max_length=20)
    format_cours = models.TextField(null = True)

class descriptif(models.Model):
    code = models.TextField(null = True)
    Titre = models.TextField(null = True)
    Credits = models.TextField(null = True)
    LieuEnseignement = models.TextField(null = True)
    gradesemestre = models.TextField(null = True)

class authentification(models.Model):
    user = models.TextField(null = True)
    password = models.TextField(null = True)
    prenom = models.TextField(null = True)
    nom = models.TextField(null = True)