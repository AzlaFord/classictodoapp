from django.db import models


class Tasks(models.Model):
    description = models.CharField(max_length=250)
    status = models.BooleanField(False)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.description}, {self.status}"

