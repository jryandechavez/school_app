# Copyright (c) 2013, school and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	columns, data = [], []

	columns = get_columns()
	print(filters)
	# data = get_data(filters=None)

	where_clause = ""
	if filters:
		where_clause = "where first_name = '{}'".format(filters.get("first_name"))

	query = "select * from `tabStudent Information`" + where_clause
	print(query)
	sts = frappe.db.sql(query, as_dict=1)
	# print (sts)
	for st in sts:
		data.append({
		"first_name": st['first_name'],
			"last_name": st['last_name'],
		})


	return columns, data

def get_columns():
	columns = [
		{"label": "First Name", "fieldname": "first_name", "fieldtype": "data", "width": "120"},
		{"label": "Last Name", "fieldname": "last_name", "fieldtype": "data", "width": "120"},

	]
	return columns


