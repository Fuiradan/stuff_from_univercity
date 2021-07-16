import requests
import json

class API(object):
	BASE_URL = 'https://api.worldoftanks.ru/wot'

	def __init__(self, app_id):
		self.app_id = app_id

	def _format_fields(self, fields):
		return ','.join(fields)

	def _api_call(self, endpoint, **kwargs):
		payload = kwargs
		payload['application_id'] = self.app_id
		r = requests.get(self.BASE_URL+endpoint, params=payload)				

		return json.dumps(r.json(), sort_keys=True, indent=4)