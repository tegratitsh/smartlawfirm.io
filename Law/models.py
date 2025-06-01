from django.db import models
from django.core.validators import RegexValidator


class Field(models.Model):
    name = models.CharField(max_length=255)
    topic_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', verbose_name="Image", blank=True, null=True)
    tag = models.CharField(max_length=128,  verbose_name="tag") # slogan
    description = models.CharField(max_length=255,  verbose_name="description", blank=True, default='')

    def __str__(self):
        return f'{self.name}'
    

class Topic(models.Model):
    
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return f'{self.name} - ({self.field})'
    

class Title(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name} - {(self.topic)}'
    


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        validators=[RegexValidator(regex=r'^\d{8,15}$', message="Le numéro doit contenir uniquement des chiffres (8-15 caractères).")]
    )
    profession = models.CharField(max_length=15, blank=True, null=True)
    description = models.TextField(blank=True, null=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone} - {self.email}"
    

class Lawyer(models.Model):

    full_name = models.CharField(max_length=128) #NOM & PRENOM
    first_name = models.CharField(max_length=128, default="fist-name")
    image = models.ImageField(upload_to='images', blank=True, null=True)
    domain = models.CharField(max_length=128, default="") # Ex : Droit commercial, Droit civil
    description = models.CharField(max_length=255, default="")  # Ex : Detail de la profession
    year_experience = models.PositiveIntegerField()
    statut = models.CharField(
        max_length=50,
        choices=[
            ('disponible', 'Disponible'),
            ('occupe', 'Occupé'),
            ('indisponible', 'Indisponible'),
        ],
        default='disponible'
    )

    def __str__(self):

        return f'{self.full_name} - {self.domain}'