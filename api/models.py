from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Schedule(models.Model):

	start_time	= models.DateTimeField(auto_now_add=False, auto_now=False)
	end_time	= models.DateTimeField(auto_now_add=False, auto_now=False)
	days		= models.CharField(max_length=250, blank=True, null=True)

class Sector(models.Model):
	#can have many trashes
	address = models.CharField(blank=True, null=True, max_length=250)
	lat     = models.CharField(max_length=250)
	lng     = models.CharField(max_length=250)
	schedules	= models.ManyToManyField(Schedule, blank=True)

class Trash(models.Model):
	#can have many states
	name = models.CharField(max_length=50, blank=True, null=True)
	sector   = models.ForeignKey(Sector, on_delete=models.CASCADE)


class TrashState(models.Model):
	TRASH_CONTENT = (
		('F', 'Full'),
		('M', 'Medium'),
		('E', 'Empty'),
	)

	trash       = models.ForeignKey(Trash, on_delete=models.CASCADE)
	content     = models.CharField(max_length=1, choices=TRASH_CONTENT)
	timestamp   = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):

	rating	= models.IntegerField()
	review	= models.CharField(max_length=300, blank=True, null=True)
	timestamp   = models.DateTimeField(auto_now_add=True)
	trash		= models.ForeignKey(Trash, on_delete=models.CASCADE)
	user		= models.ForeignKey(get_user_model(), on_delete=models.CASCADE)