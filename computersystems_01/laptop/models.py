from django.db import models
class Laptop(models.Model):
    prodid = models.CharField(max_length=10, primary_key=True)
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    price = models.FloatField(null=True)
    date_of_manf = models.DateField(null=True)
    processor = models.CharField(max_length=20)
    ram = models.CharField(max_length=5)
    size = models.IntegerField(null=True)
    screen_type = models.CharField(max_length=5)
    OS = models.CharField(max_length=30)
    Storage = models.CharField(max_length=5)

    def __str__(self):
        return self.prodid
    
class Customer(models.Model):
    custid = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=30, null=True)
    password = models.CharField(max_length=30, null=True)
    emailid = models.CharField(max_length=30, null=True)
    ph_no = models.IntegerField(null=True)
    dob = models.DateField(null=True)

    def __str__(self):
        return self.custid
    
class Technician(models.Model):
    techid = models.CharField(max_length=10, primary_key=True)
    tname = models.CharField(max_length=20, null=True)
    tusername = models.CharField(max_length=30, null=True)
    hiredate = models.DateField(null=True)
    password = models.CharField(max_length=15, null=True)
    salary = models.IntegerField(null=True)
    
    def __str__(self):
        return self.techid
    
    class Meta:
        db_table = 'laptop_technician'

class Requests(models.Model):
    reqid = models.CharField(max_length=10, primary_key=True)
    custid = models.CharField(max_length=10)
    date_of_req = models.DateField()
    repair_type = models.CharField(max_length=30)
    user_desc = models.CharField(max_length=500)

    def __str__(self):
        return self.reqid


'''class LaptopLog(models.Model):
    ACTION_CHOICES = (
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    )

    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)
    prodid = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=20)
    model_name = models.CharField(max_length=20)
    price = models.FloatField(null=True, blank=True)
    date_of_manf = models.DateField(null=True, blank=True)
    processor = models.CharField(max_length=20)
    ram = models.CharField(max_length=5)
    size = models.IntegerField(null=True, blank=True)
    screen_type = models.CharField(max_length=5)
    OS = models.CharField(max_length=30)
    Storage = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} {self.prodid.brand_name} {self.prodid.model_name}"

    class Meta:
        db_table = 'laptop_logs' '''