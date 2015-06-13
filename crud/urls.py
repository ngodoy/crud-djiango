from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ListaUsuarios.as_view(), name='index'),
    url(r'^crear/$', views.CrearUsuario.as_view(), name='crear'),
    url(r'^ver/(?P<usuarios_id>[0-9]+)', views.VerUsario.as_view(), name='ver'),
    url(r'^modificar/(?P<pk>[0-9]+)', views.ModificarUsuario.as_view(), name='modificar'),
    url(r'^borrar/(?P<usuario_id>[0-9]+)', views.BorrarUsuario.as_view(), name='borrar'),
]