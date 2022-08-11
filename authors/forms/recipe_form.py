from django.core.exceptions import ValidationError
from django import forms
from recipes.models import Recipe
from utils.django_forms import add_attr
from collections import defaultdict


class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)
        
        add_attr(self.fields.get('preparation_steps'), 'class', 'span-2')       
            
    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover'
        widgets = {
            'cover': forms.FileInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'servings_unit': forms.Select(
                choices=(
                    ('Portions', 'Portions'),
                    ('Pieces', 'Pieces'),
                ),
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Minuts', 'Minuts'),
                    ('Hs', 'Hs'),
                    
                ),
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data

        title = cleaned_data.get('title')

        if self._my_errors:
            raise ValidationError((self._my_errors))

        return super_clean

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            self._my_errors['title'].append('Title must have more than 3 chars.')

        return title

    def clean_preparation_time(self):
        field_name = 'preparation_time'
        field_value = self.cleaned_data.get(field_name)

        # if not is_positive_number(field_value):
            # self._my_errors[field_name].append('Must be positive.')

        return field_value

