from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Position(models.Model):
	title = models.CharField(max_length=50, unique=True)

	def __str__(self):
		return f"{self.title}"


class Candidate(models.Model):
	name = models.CharField(max_length=50)
	no_votes=models.IntegerField(default=0, editable=False)
	position = models.ForeignKey(Position, on_delete=models.CASCADE)
	image = models.ImageField(verbose_name="Candidate Picture", upload_to='media/images/')

	def __str__(self):
		return f'{self.name} - {self.position.title}'


class VoteStatus(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	position=models.ForeignKey(Position, on_delete=models.CASCADE)
	status=models.BooleanField(default=False)

	def __str__(self):
		return f"{self.user} - {self.position.title} - {self.status}"