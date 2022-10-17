from django.urls import path

from .views import DFPView,RepeaterView


urlpatterns = [
    path('dfp/', DFPView.as_view()),
    path('dfp', DFPView.as_view()),
    path('repeater/', RepeaterView.as_view()),
    path('repeater/', RepeaterView.as_view()),

]
