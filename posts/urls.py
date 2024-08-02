from django.urls import path
from posts.views import List


urlpatterns = [
    path("list/", List.as_view(), name="publication-list"),
    path("detail/", List.as_view(), name="detail-list"),

]