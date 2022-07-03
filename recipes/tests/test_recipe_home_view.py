from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_recipe_home_view_loads_correct_template(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')  # noqa E501

    def test_recipe_home_template_loads_recipes(self):
        """ Remember to use the function to create a recipe
         beacause django does not use
         the data base in the processing area"""
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        # response_context_recipes = response.context['recipes']  
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response.context['recipes']), 1)

    def test_recipe_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        self.assertTrue(
            '<h1>No recipes found here.</h1>', content
        )

    def test_no_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):  # noqa E501
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))   # noqa E501
        self.assertTrue(
            '<h1>No recipes found here.</h1>',
            response.content.decode('utf-8')
        )