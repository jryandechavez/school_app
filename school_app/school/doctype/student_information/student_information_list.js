/**
 * Created by vanessa on 3/25/21.
 */
 frappe.listview_settings['Student Information'] = {
        add_fields: ["student_status"],
        get_indicator: function(doc) {
            if(doc.student_status == "Enrolled") {
                return [__("Enrolled"), "green"];
            }
            else{
                return [__("Dropped"), "red"];
            }
        }
 }
