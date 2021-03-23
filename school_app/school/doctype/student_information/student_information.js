// Copyright (c) 2021, school and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Information', {
	last_name: function(frm) {
	    var fullname = frm.doc.first_name + " " + frm.doc.last_name
        frm.set_value("full_name", fullname)

	},

    birthdate: function (frm) {

	    frappe.call({
            method: "school_app.school.doctype.student_information.student_information.calculate_age",
            args:{
                "birthdate" : frm.doc.birthdate
            },
            callback: function (r) {
                var result = r.message
                console.log(result)
                frm.set_value("age", result)
            }
        })

    }
});
