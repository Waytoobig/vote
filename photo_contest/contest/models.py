from django.db import models

class Candidate(models.Model):
    CATEGORY_CHOICES = [
        ('best', 'Best Player'),
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='candidates/')
    description = models.TextField(blank=True)
    photographer = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='best')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} by {self.photographer}" if self.photographer else self.name

    @property
    def total_votes(self):
        return self.votes.count()


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    voter_name = models.CharField(max_length=100, unique=True)  # one vote per voter
    user_session = models.CharField(max_length=40)  # optional: track session too
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user_session', 'candidate']  # prevent multiple votes per candidate per session

    def __str__(self):
        return f"{self.voter_name} voted for {self.candidate.name}"
