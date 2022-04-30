from django.shortcuts import render
from django.views import generic
from .models import CreateTeam, TeamDetail

# Create your views here.

class CreateView(generic.DetailView):
    model = CreateTeam
    template_name = 'create.html'  

class TeamDetailView(generic.DetailView):
    model = TeamDetail
    template_name = 'team-detail.html'

create = CreateView.as_view()
team_detail = TeamDetailView.as_view()