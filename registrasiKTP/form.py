from django import forms
from .models import isianKTP

class tampilanformulir(forms.ModelForm):
    class Meta:
        model = isianKTP
        fields =['nomor_NIK', 'nama_lengkap','jenis_kelamin','tanggal_lahir', 'bulan_lahir','tahun_lahir','agama','status_nikah','images']

    def hapusi_nomor_NIK(self):
        verifikasi_nomor_NIK=self.cleaned_data.get('nomor_NIK')
        for instance in isianKTP.object.all():
            if instance.nomor_NIK==verifikasi_nomor_NIK:
                raise forms.ValidationError('NIK tos kapakai!')