# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("School App"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Student Information",
					"onboard": 1
				},
                {
                    "type": "doctype",
                    "name": "Courses",
                    "onboard": 1
                },
                {
                    "type": "doctype",
                    "name": "Item Category",
                    "onboard": 1,
                },
			]
		},

	]
