from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    deployed_link = models.CharField(max_length=100)
    github_link = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to='project_pics',blank=True)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images

    @classmethod
    def search_project_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_single_project(cls, project):
        project = cls.objects.get(id=project)
        return project

    class Meta:
        ordering = ['-id']



class Skill(models.Model):
    image = models.ImageField(upload_to='skill_pics',blank=True)
    name = models.CharField(max_length=20)


    def __str__(self):
        return str(self.image)

    class Meta:
        ordering = ['-id']

    def save_skill(self):
        self.save()

    @classmethod
    def fetch_all_images(cls):
        all_images = Skill.objects.all()
        return all_images