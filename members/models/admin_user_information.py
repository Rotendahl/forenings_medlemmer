from django.conf import settings
from django.db import models

from .department import Department
from .union import Union


class AdminUserInformation(models.Model):
    def __str__(self):
        return self.user.username + " admin data"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    departments = models.ManyToManyField(Department, blank=True)
    unions = models.ManyToManyField(Union, blank=True)

    @staticmethod
    def get_departments_admin(user):
        if user.is_superuser:
            return Department.objects.all()
        else:
            return Department.objects.filter(adminuserinformation__user=user)
