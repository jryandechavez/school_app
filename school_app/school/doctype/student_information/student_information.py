# -*- coding: utf-8 -*-
# Copyright (c) 2021, school and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import date, timedelta, datetime
from frappe.model.document import Document

class StudentInformation(Document):
	pass
	# def autoname(self):
	# 	self.name = "hello world"
	# def validate(self):
	# 	result = frappe.db.sql("SELECT * from `tabStudent Information`", as_dict=1)
	# 	# self.result = str(result[0]['name'])
    #
	# 	first_column = []
	# 	for i in result:
	# 		first_column.append(i['name'])
	# 	self.result = str(first_column)

	# def validate(self):
	# 	result = frappe.get_list("Student Information", {"course": "BSIT"}, ['name', 'full_name'])
    #
	# 	self.result = str(result)

	# def validate(self):
	# 	result = frappe.get_value("Student Information", "SI-2021-03-25-00001", "birthdate")
    #
	# 	self.result = str(result)


	def validate(self):
		#doctype
		if not frappe.db.exists("Courses", self.course):
			new_course = frappe.get_doc({
				"doctype": "Courses",
				"course_id": self.course,
				"course_name": self.course
			})
		#child table
			new_course.append(
				"subjects",{
					"subject_id": self.course,
					"subject_name": self.course,
				}
			)

			new_course.insert()


@frappe.whitelist()
def calculate_age(birthdate):
	converted = datetime.strptime(birthdate, '%Y-%m-%d')
	return (datetime.today() - converted) // timedelta(days=365.2425)


def sample_querry():
	result = frappe.db.sql("SELECT * from `tabStudent Information`", as_dict=1)
	print (result)


