#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
This module contains the definition of the functions that handle interfacing
with the Traffic Monitor API.
"""

from datetime import datetime
from typing import List

import requests


class Event:
	"""
	An Event represents some health event in the course of Traffic Monitor's
	polling.

	>>> data = {
	... "time": 1614887204,
	... "index": 0,
	... "description": "desc",
	... "name": "test",
	... "hostname": "host",
	... "type": "MID"
	... }
	>>> Event(data)
	Event(time=datetime.datetime(2021, 3, 4, 12, 46, 44), index=0, description='desc', name='test', hostname='host', type='MID')
	>>> str(Event(data))
	'2021-03-04 12:46:44 MID - host: desc'
	"""
	time: datetime
	index: int
	description: str
	name: str
	hostname: str
	type: str

	def __init__(self, data):
		if not isinstance(data, dict):
			raise ValueError(f"invalid event data: {data}")
		if "time" not in data:
			raise ValueError(f"malformed event (missing 'time'): {data}")
		if not isinstance(data["time"], int):
			raise ValueError(f"invalid type of 'time': {type(data['time'])}")
		if "index" not in data:
			raise ValueError(f"malformed event (missing 'index'): {data}")
		if not isinstance(data["index"], int):
			raise ValueError(f"invalid type of 'index': {type(data['index'])}")
		if "description" not in data:
			raise ValueError(f"malformed event (missing 'description'): {data}")
		if not isinstance(data["description"], str):
			raise ValueError(f"invalid type of 'description': {type(data['description'])}")
		if "name" not in data:
			raise ValueError(f"malformed event (missing 'name'): {data}")
		if not isinstance(data["name"], str):
			raise ValueError(f"invalid type of 'name': {type(data['name'])}")
		if "hostname" not in data:
			raise ValueError(f"malformed event (missing 'hostname'): {data}")
		if not isinstance(data["hostname"], str):
			raise ValueError(f"invalid type of 'hostname': {type(data['hostname'])}")
		if "type" not in data:
			raise ValueError(f"malformed event (missing 'type'): {data}")
		if not isinstance(data["type"], str):
			raise ValueError(f"invalid type of 'type': {type(data['type'])}")

		self.time = datetime.fromtimestamp(data["time"])
		self.index = data["index"]
		self.description = data["description"]
		self.name = data["name"]
		self.hostname = data["hostname"]
		self.type = data["type"]

	def __str__(self) -> str:
		return f"{self.time} {self.type} - {self.hostname}: {self.description}"

	def __repr__(self) -> str:
		return "Event(" + ", ".join([
			f"time={self.time!r}",
			f"index={self.index}",
			f"description={self.description!r}",
			f"name={self.name!r}",
			f"hostname={self.hostname!r}",
			f"type={self.type!r}"
		]) + ")"

def get_event_log(tm_url: str) -> List[Event]:
	"""
	Retrieves the event log from the /publish/EventLog TM API endpoint.

	:param tm_url: The URL of the Traffic Monitor server.
	"""
	url = tm_url.removesuffix("/") + "/publish/EventLog"
	try:
		resp = requests.get(url)
	except (requests.RequestException, OSError) as e:
		raise ConnectionError(f"request failed: {e}") from e

	response = resp.json()
	if not isinstance(response, dict):
		raise ValueError(f"Traffic Monitor returned invalid, non-JSON-object response: {response}")
	if "events" not in response:
		raise ValueError(f"Traffic Monitor responded with no 'events' property: {response}")
	events = response["events"]
	if not isinstance(events, list):
		raise ValueError(f"'events' property of response object was not an array: {events}")

	return [Event(event) for event in events]
