from django.db import models

# Create your models here.

class gameInfo(models.Model):
	result = models.CharField(max_length=255)

	def __str__(self):
		return self.result

class match_info(models.Model):
	game_assoc = models.ForeignKey(gameInfo,on_delete=models.CASCADE)
	player = models.CharField(max_length=255)
	selected_column = models.IntegerField()

	def __str__(self):
		return self.game_assoc.id
