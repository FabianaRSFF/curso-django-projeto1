from django.urls import path

from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewHome.as_view(), name="home"),
    path('recipes/search/', views.RecipeListViewSearch.as_view(), name='search'),   # noqa E501
    path('recipes/tags/<slug:slug>', views.RecipeListViewTag.as_view(), name='tag'),   # noqa E501
    path('recipes/category/<int:category_id>/', views.RecipeListViewCategory.as_view(),  # noqa E501
         name='category'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe'),
    path('recipes/api/v1/', views.RecipeListViewHomeAPI.as_view(), name='recipes_api_v1'),  # noqa E501
    path('recipes/api/v1/<int:pk>/', views.RecipeDetailAPI.as_view(), name='recipes_api_v1_detail'),  # noqa E501
    path('recipes/theory', views.theory, name='theory',),
    path(
        'recipes/api/v2/',
        views.RecipeAPIv2ViewSet.as_view({
            'get': 'list',
            'post': 'create',
            }),
        name='recipe_api_v2'
        ),
    path(
        'recipes/api/v2/<int:pk>/',
        views.RecipeAPIv2ViewSet.as_view({
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy',
            }),
        name='recipe_api_v2_detail'
        ),
    path(
        'recipes/api/v2/tag/<int:pk>/',
        views.tag_api_detail,
        name='recipe_api_v2_tag'
        ),
]
