from django.db import models


class Experiment(models.Model):
    method_choices = (
        ('PIN', 'Pin adhesion test'),
        ('ECT', 'Edge compression test'),
    )

    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=3, choices=method_choices)


class Sample(models.Model):
    experiment = models.ForeignKey(Experiment)
    value = models.FloatField()


class Roll(models.Model):
    stand_choices = (
        ('left', 'Left side'),
        ('right', 'Right side'),
    )

    datetime = models.DateTimeField(auto_now_add=True)
    stand_number = models.IntegerField()
    rollID = models.CharField(max_length=64)
    side = models.CharField(max_length=5, choices=stand_choices)
