from django.shortcuts import render
from .models import Player
# Create your views here.

def all_players_view(request):
	players = Player.objects.all()
	context = {
		'players' : players
	}
	return render(request, 'all_players.html', context)

