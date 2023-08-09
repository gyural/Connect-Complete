from django.db import models

# from accounts.models import User


class CompareList(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Obj(models.Model):
    comparelist = models.ForeignKey(CompareList, on_delete=models.CASCADE)
    object_name = models.CharField(max_length=100)
    image = models.URLField(max_length=500)

##
