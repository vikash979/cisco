from django.contrib import admin
from .models import (
    RouterDetails
)

@admin.register(RouterDetails)


class RouterData(admin.ModelAdmin):
	list_display = ('id','hostname','ip','macaddress','sapid')

# admin.site.register(UnitChapter)
# admin.site.register(ChapterTopic)
# admin.site.register(TopicSubtopic)
