from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

# now build the Django database (SQLite by default)
# python manage.py migrate
# python manage.py makemigrations [appname]
# python manage.py migrate
# Then import models module in admin.py and register your models
# python manage.py createsuperuser

# This database will be populated using the faker library
# pip install Faker
