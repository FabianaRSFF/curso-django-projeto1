from django.urls import include, path
from rest_framework.routers import SimpleRouter

from recipes import views

# TokenRefreshView,
# TokenVerifyView,


app_name = "recipes"

recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register(
    "recipes/api/v2", views.RecipeAPIv2ViewSet, basename="recipes-api"
)


urlpatterns = [
    path("", views.RecipeListViewHome.as_view(), name="home"),
    path(
        "recipes/search/", views.RecipeListViewSearch.as_view(), name="search"
    ),  # noqa E501
    path(
        "recipes/tags/<slug:slug>",
        views.RecipeListViewTag.as_view(),
        name="tag",  # noqa
    ),  # noqa E501
    path(
        "recipes/category/<int:category_id>/",
        views.RecipeListViewCategory.as_view(),  # noqa E501
        name="category",
    ),
    path("recipes/<int:pk>/", views.RecipeDetail.as_view(), name="recipe"),
    path(
        "recipes/api/v1/",
        views.RecipeListViewHomeAPI.as_view(),
        name="recipes_api_v1",  # noqa
    ),  # noqa E501
    path(
        "recipes/api/v1/<int:pk>/",
        views.RecipeDetailAPI.as_view(),
        name="recipes_api_v1_detail",
    ),  # noqa E501
    path(
        "recipes/theory",
        views.theory,
        name="theory",
    ),
    path(
        "recipes/api/v2/tag/<int:pk>/",
        views.tag_api_detail,
        name="recipe_api_v2_tag",  # noqa E501
    ),
    path("", include(recipe_api_v2_router.urls)),
]  # noqa E501
