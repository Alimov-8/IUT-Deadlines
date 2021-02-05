from django.db import models

# Create your models here.
class SophomoreDeadlines(models.Model):
    day = models.CharField(max_length=50) # Saturday
    year = models.DateTimeField() # 12.12.2020
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.day + str("  ") + str(self.year))

class SophomoreSubjects(models.Model):
    subject = models.CharField(max_length=50) #IP
    deadline = models.CharField(max_length=50) #12:00
    location = models.CharField(max_length=50) # eclass
    year = models.ForeignKey(SophomoreDeadlines, on_delete=models.CASCADE,) # Choose day

    def __str__(self):
        return self.subject

class FreshmanSubjects(models.Model):
    subject = models.CharField(max_length=50) #IP
    deadline = models.CharField(max_length=50) #12:00
    location = models.CharField(max_length=50) # eclass
    year = models.ForeignKey(SophomoreDeadlines, on_delete=models.CASCADE,) # Choose day

    def __str__(self):
        return self.subject

class SeniorSubjects(models.Model):
    subject = models.CharField(max_length=50) #IP
    deadline = models.CharField(max_length=50) #12:00
    location = models.CharField(max_length=50) # eclass
    year = models.ForeignKey(SophomoreDeadlines, on_delete=models.CASCADE,) # Choose day

    def __str__(self):
        return self.subject

class JuniorSubjects(models.Model):
    subject = models.CharField(max_length=50) #IP
    deadline = models.CharField(max_length=50) #12:00
    location = models.CharField(max_length=50) # eclass
    year = models.ForeignKey(SophomoreDeadlines, on_delete=models.CASCADE,) # Choose day

    def __str__(self):
        return self.subject


