from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name='search'),   # noqa E501
    path('recipes/category/<int:category_id>/', views.RecipeListViewCategory.as_view(), # noqa E501
         name='category'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe'),
    path('recipes/api/v1/', views.RecipeListViewHomeAPI.as_view(), name='recipes_api_v1'), # noqa E501
]
