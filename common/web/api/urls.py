# api/urls.py
from django.urls import path
from . import views
from . import views_users
from . import views_chat
from . import views_game
from django.conf import settings
from .models import Player, Friends, Messages
from django.contrib.auth import views as auth_views

# Add URLS for API
urlpatterns = [
    path('', views.getData),
	path('@me/', views.get_me),
    path('getAllUsers/', views.getAllUsers),
]

# Add URLS for users
urlpatterns += [
    path('register-42/', views_users.register_42),
    path('login_player/', views_users.login_player, name='login_player'),
    path('register/', views_users.register),
    path('logout/', views_users.logout, name='logout'),
    path('updateImg/', views_users.update_img, name='update_img'),
    path('updateData/', views_users.update_data, name='update_data'),
    path('updatePass/', views_users.update_pass, name='updatePass'),
    path('getNumberOfGames/', views_users.getNumberOfGames),
    path('getCurrentElo/', views_users.getCurrentElo),
    path('getMaxElo/', views_users.getMaxElo),
    path('getTournamentCount/', views_users.getTournamentCount),
    path('getAvgGameTime/', views_users.getAvgGameTime),
    path('getMaxWinStreak/', views_users.getMaxWinStreak),
    path('getWinrate/', views_users.getWinrate),
    path('lastGameIsWin/', views_users.lastGameIsWin),
    path('getPlayerGameData/', views_users.getPlayerGameData),
    path('getMatches/', views_users.getMatches),
    path('lastConnexion/', views_users.lastConnexion),
]

# Add URLS for chat
urlpatterns += [
    path('getSocialUser/', views_chat.getSocialUser),
    path('getChatUser/', views_chat.getChatUser),
    path('getMessages/', views_chat.getMessages),
    path('sendMessage/', views_chat.sendMessage),
    path('sendInvite/', views_chat.sendInvite),
    path('isOnline/', views_chat.isOnline),
    path('updateSocialStatus/', views_chat.updateSocialStatus),
]

# Add URLS for game

urlpatterns += [
    path('getHistoryGame/', views_game.getHistoryGame),
]