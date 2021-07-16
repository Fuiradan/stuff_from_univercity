from apiwot.api import API
import json

class Player(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

	def search_players(self, lang='ru', search='', fields=''):
		endpoint = '/account/list/'
		if type(fields) is list:
			fields = self._format_fields(fields)		
		return self._api_call(endpoint=endpoint, fields=fields, language=lang, search=search)

	def get_account_id(self, nickname=''):
		return json.loads(self.search_players(search=nickname,fields='account_id'))['data'][0]['account_id']

	def personal_data(self, account_id='', lang='ru', fields='', nickname=''):
		endpoint = '/account/info/'
		if type(fields) is list:
			fields = self._format_fields(fields)
		if nickname:			
			account_id = self.get_account_id(nickname=nickname)

		return self._api_call(endpoint=endpoint, 
							  fields=fields, 
							  language=lang, 
							  account_id=account_id)

	def player_vehicles(self, account_id='', lang='ru', fields='', nickname=''):
		endpoint = '/account/tanks/'
		if type(fields) is list:
			fields = self._format_fields(fields)
		if nickname:			
			account_id = self.get_account_id(nickname=nickname)
		return self._api_call(endpoint=endpoint, 
							  fields=fields, 
							  language=lang, 
							  account_id=account_id)

	def player_achievements(self, account_id='', lang='ru', fields='', nickname=''):
		endpoint = '/account/achievements/'
		if type(fields) is list:
			fields = self._format_fields(fields)
		if nickname:			
			account_id = self.get_account_id(nickname=nickname)
		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)