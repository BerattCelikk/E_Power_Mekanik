from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100,verbose_name="Name Surname")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Message Content")
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name="Date Sent")
    
    def __str__(self):
        return f"{self.name} - {self.email}"
    
     