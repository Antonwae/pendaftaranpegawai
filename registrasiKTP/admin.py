from django.contrib import admin
from .models import isianKTP
class isianKTPAdmin(admin.ModelAdmin):
    list_display = (
        ('nomor_NIK'),
        ('nama_lengkap'),
        ('jenis_kelamin'),
        ('tanggal_lahir'),
        ('bulan_lahir'),
        ('tahun_lahir'),
        ('agama'),
        ('status_nikah')

    )
admin.site.register(isianKTP,isianKTPAdmin)

