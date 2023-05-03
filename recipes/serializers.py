from rest_framework import serializers

from authors.validators import AuthorRecipeValidator
from tag.models import Tag

from .models import Recipe


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'author',
            'category', 'tags', 'public', 'preparation',
            'tag_objects', 'tag_links',
            'preparation_time', 'preparation_time_unit', 'servings',
            'servings_unit',
            'preparation_steps', 'cover'
        ]
    id = serializers.IntegerField()
    description = serializers.CharField(max_length=165)
    title = serializers.CharField(max_length=65)
    public = serializers.BooleanField(source='is_published', read_only=True)
    preparation = serializers.SerializerMethodField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    tag_objects = TagSerializer(
        many=True, source='tags', read_only=True,
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        read_only=True,
        view_name='recipes:recipe_api_v2_tag'
    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'

    def validate(self, attrs):
        super_validate = super().validate(attrs)

        AuthorRecipeValidator(
            data=attrs,
            ErrorClass=serializers.ValidationError,
        )
        return super_validate

    def save(self, **kwargs):
        return super().save(**kwargs)

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
