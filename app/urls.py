from django.urls import path,include
from .views import KitabListView
from .views import KitabDetailView,KitabCreateView,KitabDeleteView,KitabUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',KitabListView.as_view(template_name =  'index.html'),name='index'),
    path('<slug:slug>',KitabDetailView.as_view(template_name =  'book_detail.html'), name = "book-detail"),
    path('add/',KitabCreateView.as_view(),name="book-create"),
    path('<slug>/delete',KitabDeleteView.as_view(template_name = 'confirm-delete.html') ),
    path('<slug>/update',KitabUpdateView.as_view() ),

]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)