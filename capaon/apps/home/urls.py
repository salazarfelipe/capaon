from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('capaon.apps.home.views',
	url(r'^$','index_view', name='vistaInicial'),
	url(r'^register/$','construccion', name = 'vista_registro'),
	url(r'^MisionVision/$','mv_view', name = 'vista_MisionVision'),
	url(r'^capacitacion/$','cursos_view', name = 'vista_Cursos'),
	url(r'^capacitacion/(\d{1,2})$','Infocursos_view', name = 'vista_InfoCursos'),
	url(r'^contacto/$','contact_view', name = 'vista_Contacto'),
	)