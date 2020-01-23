from rest_framework import serializers

from .models import (Sector, Schedule, Trash, TrashState)

class ScheduleSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Schedule
		fields = (
				'start_time',
				'end_time',
		 		'days'
		 		)

class SectorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sector
		fields = (
				'address',
				'lat',
		 		'lng',
		 		)

class TrashSerializer(serializers.ModelSerializer):
	sector = SectorSerializer()
	class Meta:
		model = Trash
		fields = (
				'name',
				'sector',
		 		)
