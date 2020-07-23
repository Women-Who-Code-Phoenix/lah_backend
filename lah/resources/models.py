from django.db import models

from .field_choices import STATUS, ACTIVE


class Resource(models.Model):
    description = models.CharField(max_length=528)
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=16, choices=STATUS, default=ACTIVE)


class Tag(models.Model):
    name = models.CharField(max_length=180)
    resource = models.ForeignKey(
        "Resource", on_delete=models.SET_NULL, null=True, related_name="tags"
    )

    def __str__(self):
        return self.name
