from django.db import models

class CV(models.Model):
    first_name = models.CharField(max_length=100, default="Akın")
    last_name = models.CharField(max_length=100, default="Tanrıverdi")
    email = models.EmailField(default="akntanrverdi2@gmail.com")
    phone_number = models.CharField(max_length=20, default="05380891401")
    job_title = models.CharField(max_length=100, default="Information Systems Engineer")
    bio = models.TextField(default="Passionate about technology and development, with a focus on IT systems. Enthusiastic learner and problem solver.")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
