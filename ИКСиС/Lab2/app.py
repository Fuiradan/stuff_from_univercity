from apiwot.player import Player
from apiwot.tankopedia import Tankopedia
from apiwot.vehicle import Vehicle

app_id = '1c9121ae8b3f07b7cee4c618ebbe6cda' #application_id - уникальный код приложения, обязятелен для всех запросов

p = Player(app_id)
t = Tankopedia(app_id)
v = Vehicle(app_id)

#out = p.search_players(search='fdsf')
#out = p.player_achievements(nickname='KorbenDallas')
out = t.vehicles(nation="ussr", tier="10")

file = open('out.html', 'w')
file.write(out)
file.close()

