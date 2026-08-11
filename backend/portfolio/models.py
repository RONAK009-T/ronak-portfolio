from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=100)
    technologies = models.TextField(help_text="Comma-separated list of technologies")
    features = models.TextField(help_text="Newline-separated list of features")
    github_url = models.URLField(max_length=500, blank=True, null=True)
    live_url = models.URLField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Fallback external image URL")
    local_path = models.CharField(max_length=500, blank=True, null=True, help_text="Local directory path of the project manage.py")
    local_port = models.IntegerField(blank=True, null=True, help_text="Port number to launch the project server locally")
    featured = models.BooleanField(default=False)

    created_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('AI/Data Science', 'AI & Data Science'),
        ('Tools', 'Tools & Others'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.PositiveIntegerField(default=80, help_text="Skill proficiency from 0 to 100")
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g. Code, Database, Globe)")

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300, blank=True, help_text="Comma-separated list of technologies used")
    responsibilities = models.TextField(help_text="Newline-separated list of achievements/responsibilities")
    start_date = models.CharField(max_length=100, help_text="e.g. Jan 2024")
    end_date = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Present or Dec 2024")
    current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    course = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=100, help_text="e.g. 2021 - 2025")
    grade_or_skills = models.CharField(max_length=200, blank=True, help_text="e.g. CGPA: 9.2 or Core Python")
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.course} - {self.institute}"


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Resume(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='resumes/')
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_active:
            # Set all other resumes to inactive
            Resume.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} (Active: {self.is_active})"


class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField(max_length=500)
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name (e.g. Github, Linkedin, Mail)")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.platform


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
