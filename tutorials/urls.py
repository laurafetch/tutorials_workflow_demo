from django.urls import path
from tutorials import views as tutorials_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', tutorials_views.index.as_view(), name='home'), # renders homepage as name home to the index view
    path('api/tutorials/', tutorials_views.tutorial_list),
    path('api/tutorials/<int:pk>/', tutorials_views.tutorial_detail),
    path('api/tutorials/published/', tutorials_views.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)