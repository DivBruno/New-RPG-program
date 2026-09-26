from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, MaxValueValidator, MinValueValidator

def skill_validator():
    return True

def items_validator():
    return True

class Background(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    skills = models.JSONField(validators=[skill_validator, MaxLengthValidator(2), MinLengthValidator(2)])

class Status(models.Model):
    health_points = models.IntegerField()
    sanity_points = models.IntegerField()
    effort_points = models.IntegerField()
    defense = models.IntegerField()

    speed = models.FloatField()
    carry_capacity = models.FloatField()

class Attributes(models.Model):
    strength = models.IntegerField(default=1)
    agility = models.IntegerField(default=1)
    vigor = models.IntegerField(default=1)
    intellect = models.IntegerField(default=1)
    presence = models.IntegerField(default=1)

    def __str__(self):
            return f"STR: {self.strength} | AGI: {self.agility} | VIG {self.vigor} | INT {self.intellect} | PRE {self.presence}"

class Extras(models.Model):
    abilities = models.TextField()
    annotation = models.TextField()
    proficiency = models.TextField()
    disorders = models.TextField()
    lore = models.TextField()
    relationships = models.TextField()
    appearance = models.TextField()


class Character(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    money = models.IntegerField()
    daily_money = models.IntegerField()
    # in the future, change the on delete cascade to something safer
    background = models.ForeignKey(Background, on_delete=models.CASCADE)
    status = models.OneToOneField(Status, on_delete=models.CASCADE)
    attributes = models.OneToOneField(Attributes, on_delete=models.CASCADE)
    extras = models.OneToOneField(Extras, on_delete=models.CASCADE, null = True)
    # json fields, they're gonna have a their own validators
    skills = models.JSONField(validators=[skill_validator], null = True)
    items = models.JSONField(validators=[items_validator], null = True)