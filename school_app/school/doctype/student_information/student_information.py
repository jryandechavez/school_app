# -*- coding: utf-8 -*-
# Copyright (c) 2021, school and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import date, timedelta, datetime
from frappe.model.document import Document

class StudentInformation(Document):
	pass


@frappe.whitelist()
def calculate_age(birthdate):
	converted = datetime.strptime(birthdate, '%Y-%m-%d')
	return (datetime.today() - converted) // timedelta(days=365.2425)
