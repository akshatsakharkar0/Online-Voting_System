from django.db import models
from django.contrib.auth.models import User

class Election(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=200)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE, null=True, blank=True)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        if self.election:
            return f"{self.user.username} - {self.election.name}"
        else:
            return f"{self.user.username} - No election assigned"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    election = models.ForeignKey(Election, on_delete=models.CASCADE, default=1)
    voted = models.BooleanField(default=False)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.user.username} voted for {self.candidate} in {self.election}'