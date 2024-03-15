from django.db import models

# Create your models here.
# models.py

from django.db import models

class ServiceRequest(models.Model):
    TYPES = (
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
        # Add more types as needed
    )
    type = models.CharField(max_length=50, choices=TYPES)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.type} - {self.created_at}'


# models.py

from django.db import models

class ServiceRequest(models.Model):
    TYPES = (
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
        # Add more types as needed
    )
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    )
    type = models.CharField(max_length=50, choices=TYPES)
    details = models.TextField()
    attached_file = models.FileField(upload_to='attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.type} - {self.created_at}'
