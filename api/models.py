from django.db import models

# Create your models here.

class Trash(models.Model):
	#can have many states
	name = models.CharField(max_length=1, blank=True, null=True)



class TrashState(models.Model):
	TRASH_CONTENT = (
		('F', 'Full'),
		('M', 'Medium'),
		('E', 'Empty'),
	)

	trash       = models.ForeignKey(Trash, on_delete=models.CASCADE)
	content     = models.CharField(max_length=1, choices=TRASH_CONTENT)
	timestamp   = models.DateTimeField(auto_now_add=True)

class Sector(models.Model):
	#can have many trashes
	address = models.CharField(blank=True, null=True, max_length=250)
	lat     = models.CharField(max_length=250)
	lng     = models.CharField(max_length=250)
	trash   = models.ForeignKey(Trash, on_delete=models.CASCADE)
