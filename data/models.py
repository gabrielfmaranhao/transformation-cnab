from django.db import models
 
class Data(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    store_owner = models.CharField(max_length=30)
    store_name = models.CharField(max_length=30)
    recipient_cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    date = models.DateField()
    hour = models.TimeField()
    type = models.ForeignKey("trasation.Trasation", on_delete=models.CASCADE, related_name="datas")


