from django.db import models

# Create your models here.


# Title Section
class Title(models.Model):
  titleDescription = models.CharField(max_length=250)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.titleDescription[:10]




# About Section
class About(models.Model):
  """Model definition for about."""

  profilePicture = models.ImageField(upload_to='uploaded/')
  aboutDescription = models.CharField(max_length=250)
  resume = models.FileField(upload_to='uploaded/')
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.aboutDescription



# Skills Section
class Category(models.Model):
  name = models.CharField(max_length=20)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = "Skill"
    verbose_name_plural = "Skills"

  def __str__(self):
    return self.name


class Skills(models.Model):
  cat = models.ForeignKey(Category, on_delete=models.CASCADE)

  skill = models.CharField(max_length=20)


# Project Section

class Projects(models.Model):
  projectTitle = models.CharField(max_length=250)
  projectDes = models.TextField(blank=False)
  tools = models.CharField(max_length=30)
  gitLink = models.URLField(max_length=200, blank=True)
  liveLink = models.URLField(max_length=200)
  projectImage = models.ImageField(upload_to='uploaded/')

  def splitTools(self):
    return self.tools.split(",")

  def __str__(self):
    return self.projectTitle

# Social Section
class Social(models.Model):
  git = models.URLField(max_length=100)
  linkedIN = models.URLField(max_length=100)
  mail = models.URLField(max_length=100)
  leetCode = models.URLField(max_length=100)
  devTO = models.URLField(max_length=100)
  updated = models.DateTimeField(auto_now=True)



  def __str__(self):
    return f'Social Account (self.id)'