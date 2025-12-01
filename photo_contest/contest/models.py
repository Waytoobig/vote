from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Candidate(models.Model):
    CATEGORY_CHOICES = [
        ('nature', 'Nature'),
        ('portrait', 'Portrait'),
        ('urban', 'Urban'),
        ('wildlife', 'Wildlife'),
        ('abstract', 'Abstract'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100, help_text="Title of the photograph")
    image = models.ImageField(upload_to='candidates/')
    description = models.TextField(blank=True, help_text="Brief description of the photo")
    photographer = models.CharField(max_length=100, blank=True, help_text="Name of the photographer")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} by {self.photographer}" if self.photographer else self.name

    @property
    def total_votes(self):
        return self.votes.count()

class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    user_session = models.CharField(max_length=40)  # Store session key instead of user
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user_session', 'candidate']

    def __str__(self):
        return f"Vote for {self.candidate.name}"