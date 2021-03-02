from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
pilihan_jenis_kelamin=(
    ('laki-laki','LAKI-LAKI'),
    ('perempuan','PEREMPUAN')
)

pilihan_bulan_lahir=(
    ('januari','JANUARI'),
    ('februari','FEBRUARI'),
    ('maret','MARET'),
    ('april','APRIL'),
    ('mei','MEI'),
    ('juni','JUNI'),
    ('juli','JULI'),
    ('agustus','AGUSTUS'),
    ('september','SEPTEMBER'),
    ('oktober','OKTOBER'),
    ('nopember','NOVEMBER'),
    ('desember','DESEMBER'),

)
pilihan_agama=(
    ('islam','ISLAM'),
    ('katholik','KATHOLIK'),
    ('kristen','KRISTEN'),
    ('hindu','HINDU'),
    ('konghuchu','KONGHUCHU'),
    ('budha','BUDHA'),
    ('lainnya','LAINNYA')
)
status_nikah=(
    ('belum kawin','BELUM KAWIN'),
    ('kawin','KAWIN')
)


class isianKTP(models.Model):
    nomor_NIK=models.IntegerField()
    nama_lengkap=models.CharField(max_length=150)
    jenis_kelamin=models.CharField(max_length=50,choices=pilihan_jenis_kelamin)
    tanggal_lahir=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(31)])
    bulan_lahir=models.CharField(max_length=50,choices=pilihan_bulan_lahir)
    tahun_lahir=models.IntegerField(validators=[MinValueValidator(1920),MaxValueValidator(2021)])
    agama=models.CharField(max_length=20,choices=pilihan_agama)
    status_nikah=models.CharField(max_length=20,choices=status_nikah)
    images=models.ImageField(null=True,blank=False, upload_to='gudang foto ktp' )

class pekerja(models.Model):
    nomor_pekerja=models.IntegerField()