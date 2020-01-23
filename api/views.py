from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import (TrashSerializer)

from .models import (Trash, )
# Create your views here.


class TrashViewSet(ModelViewSet):

	serializer_class = TrashSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
		return Trash.objects.all()
