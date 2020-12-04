from django.db import models
from django.utils.text  import slugify

class Janrlar(models.Model):
    janr_adi        = models.CharField(max_length=50,null=True,blank=False,unique=True,verbose_name="Kitablarin janri")
    qeyd_tarix      = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.janr_adi

class Yazar(models.Model):
    yazar_adi       = models.CharField(max_length=50,null=True,blank=False)
    yazar_soyadi    = models.CharField(max_length=50,null=True,blank=False)
    yazar_janr      = models.ForeignKey(Janrlar,null=True,blank=False,on_delete = models.CASCADE)
    qeyd_tarix      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.yazar_adi


class Kitab(models.Model):
    kitab_ad        = models.CharField(max_length=100,null=True,blank=True,verbose_name="Kitab adi",unique=True)
    kitab_janr      = models.ForeignKey(Janrlar,null=True,blank=False,on_delete = models.CASCADE)
    kitab_yazar     = models.ForeignKey(Yazar,null=True,blank=False,on_delete = models.CASCADE)
    kitab_seh       = models.IntegerField(null=False,blank=False,default=0)
    stokda          = models.BooleanField(null=True,blank=False,default=True)
    kitab_onsoz     = models.TextField(null=True,blank=False)
    sekil           = models.ImageField(null = True,blank = True,upload_to='images/')
    slug            = models.SlugField(null=True,blank=False,unique=True)
    qeyd_tarix      = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.kitab_ad

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.kitab_ad)
        super(Kitab, self).save(*args, **kwargs)

