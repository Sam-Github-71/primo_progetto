from django.urls import path
from prima_app.views import homepage
from prima_app.views import welcome
from prima_app.views import lista
from prima_app.views import chi_siamo
from prima_app.views import variabili
from prima_app.views import index
app_name="seconda_app"
urlpatterns=[
  path('es_if', es_if, name='es_if')
  ]