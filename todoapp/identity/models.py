from django.db import models



class Identity(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    categories = models.JSONField()

    def __str__(self):
        return self.username
    
    def check_password(self, password):
        print(self.password, password)
        return self.password == password