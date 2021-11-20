from django.db import models
from jsonfield import JSONField


class Seller(models.Model):
    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class BackupHandle(models.Model):
    name_user = models.CharField(max_length=200)
    name_id = models.CharField(max_length=200)
    old_handle = JSONField(null=True, blank=True, default=dict)

    def __str__(self) -> str:
        return self.name
