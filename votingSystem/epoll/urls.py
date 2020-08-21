from django.urls import path

from . import views

urlpatterns = [
	path("", views.home_view, name="home"),
	path('login/', views.login_view, name="login"),
	path('register/', views.register_view, name="register"),
	path('dashboard/', views.dashboard_view, name="dashboard"),
	path('logout/', views.logout_view, name='logout'),
	path('position/', views.position_view, name='position'),
	path('candidate/<int:pos>/', views.candidate_view, name="candidate"),
	path('candidate/detail/<int:id>/', views.candidateDetail_view, name="detail"),
	path('results/', views.result_view, name='result'),
	path('changePassword/', views.changePassword_view, name='changePassword'),
	path('editProfile/', views.editProfile_view, name='editProfile'),
]