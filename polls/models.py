from django.db import models

class Users(models.Model):
    user = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    # db_table = 'users'
    def __str__(self):
        return self.user_name

class Messages(models.Model):
    message = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(Users, on_delete=models.PROTECT)
    text = models.CharField(max_length=200)
    # db_table = 'messages'

    def __str__(self):
        return self.text
