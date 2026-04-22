from django.db import models

# 🧠 Skill Model (FIRST)
class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 🚀 Project Model (SECOND)
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True, null=True)
    live_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


# 👤 Profile Model (LAST)
class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()

    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.name