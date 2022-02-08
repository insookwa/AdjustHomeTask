from django.urls import path,include
from data.views import UploadFileView

urlpatterns = [

    path('upload/',UploadFileView.as_view(),name = 'upload-file')
]
