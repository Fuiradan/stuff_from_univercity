from apiwot.api import API

class Tankopedia(API):

	def __init__(self, app_id):
		API.__init__(self,app_id)

	def vehicles(self, fields='', language='ru', tank_id='', nation='', tier=''):
		endpoint = '/encyclopedia/vehicles/'	

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language, tank_id=tank_id, nation=nation, tier=tier)

	def vehicle_profile(self, fields='', language='ru', tank_id = None):
		endpoint = '/encyclopedia/vehicleprofile/'	

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language, tank_id=tank_id)

	def info(self, fields='', language='ru'):
		endpoint = '/encyclopedia/info/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)

	def maps(self, fields='', language='ru'):
		endpoint = '/encyclopedia/arenas/'

		if type(fields) is list:
			fields = self._format_fields(fields)

		return self._api_call(endpoint=endpoint, fields=fields, language=language)