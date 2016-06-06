from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactModelAdmin(admin.ModelAdmin):
	list_display = ["email", "name", "message", "time_message_sent", "contacted"]
	#list_display_links = ["name"] #samo da mozemo da kliknemo i na ime i da nam otvori kontakt
	list_editable = ["contacted"] 
	list_filter = ["time_message_sent"]

	search_fields = ["name", "message"]

	class Meta:
		model = Contact

admin.site.register(Contact, ContactModelAdmin)