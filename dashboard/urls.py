from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('view/',views.viewfunction,name='view'),
    path('notes/',views.notesfunction,name='notes'),
    path('addnote/',views.addnotefunction,name='addnote'),
    path('delete/<int:nid>',views.deletefunction,name='delete'),
    path('logout/',views.logoutfunction,name='logout'),
    

]
