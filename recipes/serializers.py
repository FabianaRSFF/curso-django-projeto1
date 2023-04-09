from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=165)
    title = serializers.CharField(max_length=65)
 
