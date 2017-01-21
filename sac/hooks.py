# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "sac"
app_title = "SAC"
app_publisher = "Tut Tangtragulcharoen"
app_description = "extension of ERPNext customized for Sri Ayudhya Concrete"
app_icon = "octicon octicon-book"
app_color = "#589494"
app_email = "n/a"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sac/css/sac.css"
# app_include_js = "/assets/sac/js/sac.js"

# include js, css files in header of web template
# web_include_css = "/assets/sac/css/sac.css"
# web_include_js = "/assets/sac/js/sac.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "sac.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "sac.install.before_install"
# after_install = "sac.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sac.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sac.tasks.all"
# 	],
# 	"daily": [
# 		"sac.tasks.daily"
# 	],
# 	"hourly": [
# 		"sac.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sac.tasks.weekly"
# 	]
# 	"monthly": [
# 		"sac.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "sac.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sac.event.get_events"
# }

