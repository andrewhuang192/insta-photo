from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('photos/', views.photos_index, name='index'),
  path('profile/', views.profile, name='profile'),
  path('photos/<int:photo_id>/', views.photos_detail, name='detail'),
  path('photos/create/', views.PhotoCreate.as_view(), name='photos_create'),
  path('photos/<int:pk>/update/', views.PhotoUpdate.as_view(), name='photos_update'),
  path('photos/<int:pk>/delete/', views.PhotoDelete.as_view(), name='photos_delete'),
  path('photos/<int:photo_id>/add_comment/', views.add_comment, name='add_comment'),
  path('photos/<int:photo_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
  path('photos/<int:photo_id>/assoc_tag/<int:tag_id>/delete/', views.delete_tag, name='delete_tag'),

]
