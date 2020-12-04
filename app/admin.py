from django.contrib import admin
from .models import Janrlar,Yazar,Kitab
from django.urls import reverse
from urllib.parse import urlencode
from django.utils.html import format_html


admin.site.site_header = 'Alishan Charkaz '
admin.site.site_title = "Alishan Charkaz"


admin.site.register(Janrlar)

@admin.register(Kitab)
class KitabAdmin(admin.ModelAdmin):
    list_display = ['kitab_ad','kitab_janr','kitab_yazar','stokda','sekil']


@admin.register(Yazar)
class YazarAdmin(admin.ModelAdmin):
    list_display = ['yazar_adi','yazar_soyadi','yazar_janr','qeyd_tarix','yazdigi_kitablar']

    def yazdigi_kitablar(self, obj):
        count = obj.kitab_set.count()
        url = (
            reverse("admin:app_kitab_changelist")
            + "?"
            + urlencode({"Yazar__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Kitab</a>', url, count)

    yazdigi_kitablar.short_description = "Kitablar"


    list_filter = ("qeyd_tarix",'yazar_janr' )
    search_fields = ("yazar_adi__icontains", )
    