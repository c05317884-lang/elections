# election_project/election_app/urls.py
from django.urls import path
from .views import (
    IndexView, SetupAdminView, LoginView, LogoutView, DashboardView, CandidatesView,
    AddCandidateView, EditCandidateView, DeleteCandidateView, VotersView,
    AddVoterView, EditVoterView, DeleteVoterView, ResultsView, ResultsJSONView, DownloadPDFView, DownloadWordView, SettingsView,
    VoterDashboardView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('setup-admin/', SetupAdminView.as_view(), name='setup_admin'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('candidates/', CandidatesView.as_view(), name='candidates'),
    path('candidates/add/', AddCandidateView.as_view(), name='add_candidate'),
    path('candidates/edit/<int:pk>/', EditCandidateView.as_view(), name='edit_candidate'),
    path('candidates/delete/<int:pk>/', DeleteCandidateView.as_view(), name='delete_candidate'),
    path('voters/', VotersView.as_view(), name='voters'),
    path('voters/add/', AddVoterView.as_view(), name='add_voter'),
    path('voters/edit/<int:pk>/', EditVoterView.as_view(), name='edit_voter'),
    path('voters/delete/<int:pk>/', DeleteVoterView.as_view(), name='delete_voter'),
    path('results/', ResultsView.as_view(), name='results'),
    path('results/json/', ResultsJSONView.as_view(), name='results_json'),
    path('results/download/pdf/', DownloadPDFView.as_view(), name='download_pdf'),
    path('results/download/word/', DownloadWordView.as_view(), name='download_word'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('vote/', VoterDashboardView.as_view(), name='voter_dashboard'),
]