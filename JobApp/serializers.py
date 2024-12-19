from rest_framework import serializers
from JobApp.models import CommentModel

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=CommentModel
        fields='__all__'
