from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=55)
    shop = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")
    def __str__(self):
        return self.name

class Debtor(models.Model):
    debtor = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True)
    amount = models.PositiveIntegerField()
    borrowed_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Debtor")
        verbose_name_plural = ("Debtors")
    def __str__(self):
        return f"{self.debtor} {self.amount}"


class Creditor(models.Model):
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    borrowed_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Creditor")
        verbose_name_plural = ("Creditors")
    def __str__(self):
        return f"{self.name} "

class MyDebts(models.Model):
    creditor = models.ForeignKey(Creditor,on_delete=models.CASCADE,blank=True) 
    amount = models.PositiveIntegerField(blank=True) 

    def save(self, *args, **kwargs):
        self.amount = self.creditor.amount
        return super().save(*args, **kwargs)
    class Meta:
        verbose_name = ("MyDebt")
        verbose_name_plural = ("MyDebts")
    def __str__(self):
        return f"Creditor: {self.creditor} - - - - -  Amount Owed: {self.amount}"

