from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("oil management"),
			"items": [
				{
					"type": "doctype",
					"name": "Order Go",
					"onboard": 1,
				}
				
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Branch Ypc",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Truck",
					"onboard": 1,
				}
			]
		},
		
	]
