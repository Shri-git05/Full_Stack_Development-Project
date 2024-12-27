from django.urls import path
from translator import views

urlpatterns = [
    path("audio-recognition/", views.audio_recognition_page, name="audio_recognition"),
    path("recognize-and-translate/", views.recognize_and_translate, name="recognize_and_translate"),
    path("next-page/", views.next_page, name="next_page"),
]
