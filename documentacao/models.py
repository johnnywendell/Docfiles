from django.db import models
from django.urls import reverse_lazy
from core.models import TimeStampedModel
from django.conf import settings
from django.db.models.signals import pre_save, post_save

class Unidade(models.Model):
    unidade = models.CharField(max_length=30, unique=True)
    class Meta:
        ordering = ('unidade',)
    def __str__(self):
        return self.unidade
    
class TipoDocumento(models.Model):
    tipo = models.CharField(max_length=30, unique=True)
    cod = models.CharField(max_length=3, unique=True)
    class Meta:
        ordering = ('tipo',)
    def __str__(self):
        return self.cod
    
class Departamento(models.Model):
    dept = models.CharField(max_length=30, unique=True)
    cod = models.CharField(max_length=10, unique=True)
    class Meta:
        ordering = ('dept',)
    def __str__(self):
        return self.cod 

class Documento(TimeStampedModel): 
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    documento = models.IntegerField()
    titulo = models.CharField('Título',max_length=80)
    rev = models.IntegerField('Revisão',default=0)
    slug = models.SlugField(default="", null=False)
    unidade = models.ForeignKey(Unidade, on_delete=models.CASCADE)
    tipodocumento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta: 
        unique_together = ('tipodocumento','departamento')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{}-{}-{}'.format(self.tipodocumento,self.departamento,str(self.documento).zfill(4))
    
    def save(self, *args, **kwargs):
        if not self.id:  
            ultimo_documento = Documento.objects.filter(tipodocumento=self.tipodocumento,departamento=self.departamento).order_by('-documento').first()
            if ultimo_documento:
                self.documento = ultimo_documento.documento + 1
            else:
                self.documento = 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('documentacao:doc_detail', kwargs={'slug': self.slug})
    
class Arquivo(TimeStampedModel):
    bmf = models.ForeignKey(Documento, on_delete=models.CASCADE)
    doc = models.FileField('documento',upload_to='docfiles/', max_length=100, blank=True, null=True)


##############################################################################################
import string, random
from django.utils.text import slugify 
  
def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(instance.titulo) 
    Klass = instance.__class__ 
    qs_exists = Klass.objects.filter(slug = slug).exists() 
      
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug, randstr = random_string_generator(size = 6)) 
        return unique_slug_generator(instance, new_slug = new_slug) 
    return slug 

def pre_save_receiver(sender, instance, *args, **kwargs): 
   if not instance.slug: 
       instance.slug = unique_slug_generator(instance) 
  
pre_save.connect(pre_save_receiver, sender = Documento)