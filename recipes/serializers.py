from rest_framework import serializers


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=165)
    title = serializers.CharField(max_length=65)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField()
    
    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'
 
