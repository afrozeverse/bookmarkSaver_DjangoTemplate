from django.urls import path
from . import views

urlpatterns = [
    path('bookmarks-list/', views.bookmarksList, name='bookmarksList'),
    path('add-bookmark/', views.addBookmark, name='addBookmark'),
    path('delete-bookmark/<int:id>/', views.deleteBookmark, name='deleteBookmark'),
    path('edit-bookmark/<int:id>/', views.editBookmark, name='editBookmark'),
]