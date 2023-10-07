from django.db import models

# 儲存文章的資料表
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)

    def __str__(self) -> str:
        return self.title
    
class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f   = models.BooleanField()
    date_f   = models.DateField(auto_now=True)
    char_f   = models.CharField(max_length=20, unique=True)
    datetime_f=models.DateTimeField(auto_now_add=True)
    decimal_f= models.DecimalField(max_digits=10, decimal_places=2)
    float_f  = models.FloatField(null=True)
    int_f    = models.IntegerField(default=2010)
    text_f   = models.TextField()

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default='http://i.imgur.com/Ous4iGB.png')

    def __str__(self):
        return self.name
    
class Ch07_Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.CASCADE, verbose_name='型號')
    nickname = models.CharField(max_length=15, default='超值二手機', verbose_name='摘要')
    description = models.TextField(default='暫無說明')
    year = models.PositiveIntegerField(default=2016, verbose_name='出廠年份')
    price = models.PositiveIntegerField(default=0, verbose_name='價格')

    def __str__(self):
        return self.nickname
    
class PPhoto(models.Model):
    product = models.ForeignKey(Ch07_Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default='產品照片')
    url = models.URLField(default='http://i.imgur.com/Z230eeq.png')
    media = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.description
    
class ch08_Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status

class ch08_Post(models.Model):
    mood = models.ForeignKey('ch08_Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='不願意透漏身份的人')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
