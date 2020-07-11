from django.db import models

class Covid(models.Model):
    dia = models.DateTimeField()
    total_contagios = models.CharField(max_length=100)
    total_recuperados = models.CharField(max_length=100)
    diarios = models.CharField(max_length=100)

    def publish(self):
        self.save()