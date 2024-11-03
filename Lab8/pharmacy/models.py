from django.db import models

class Medicine(models.Model):
    registration_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    manufacture_date = models.DateField()
    shelf_life = models.IntegerField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prescription_required = models.BooleanField()

    def __str__(self):
        return self.name

class Supplier(models.Model):
    supplier_code = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=100)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.supplier_name

class Supply(models.Model):
    supply_code = models.AutoField(primary_key=True)
    supply_date = models.DateField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f"Supply {self.supply_code} of {self.medicine}"
