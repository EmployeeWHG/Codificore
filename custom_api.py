# Copyright (c) 2023, Frutter Software Labs (P) Ltd and contributors
# For license information, please see license.txt

import frappe

# for get customer details with address html field
@frappe.whitelist(allow_guest=True)
def get_customer_profile(customer):
    customer_data = frappe.get_doc("Customer",customer)
    customr_nm = customer_data.customer_name
    dob = customer_data.fsl_dob
    mail = customer_data.email_id
    phone = customer_data.mobile_no
    pan = customer_data.pan
    demat = customer_data.fsl_demat_id
    support = customer_data.fsl_support_code    
    
    address1 = ""
    address2 = ""
    city = ""
    state = ""
    postal = "" 
    address = frappe.get_last_doc("Address",filters={'address_title' :customer,"address_type":"Billing"})
    address1 = address.address_line1
    address2 = address.address_line2
    city = address.city 
    state = address.state 
    postal = address.pincode  

    
    tot_address = (address1,address2,city,state,postal)
    frappe.response["message"] = {
        "data": {
            "customer_name": customr_nm,
            "fsl_dob":dob,
            "email_id":mail,
            "mobile_no":phone,
            "pan":pan,
            "fsl_demat_id": demat,
            "fsl_support_code":support,
            "address":tot_address
    }
    }
   
