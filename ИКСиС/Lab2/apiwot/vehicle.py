from apiwot.api import API

class Vehicle(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

	def vehicle_stats(self, lang='ru', fields='', account_id=''):

		endpoint = '/tanks/stats/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)

	def vehicle_achievements(self, lang='ru', fields='', account_id=''):

		endpoint = '/tanks/achievements/'

		if type(fields) is list:
			fields = self._format_fields(fields)		

		return self._api_call(endpoint=endpoint, fields=fields, language=lang, account_id=account_id)