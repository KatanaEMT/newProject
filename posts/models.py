from django.db import models


class Publication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(verbose_name="Описание", null=True, blank=False)

    def __str__(self):
        return self.name
