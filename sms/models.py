from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    class Meta:
        ordering = ('first_name',)
        
    def __str__(self):
        return self.first_name
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def get_phone(self):
        return self.phone

class Service(models.Model):
    service_name = models.CharField(max_length=30)
    message = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    class Meta:
        ordering = ('service_name',)

    def __str__(self):
        return self.service_name

    def get_message(self):
        return self.message
    
    def get_employee(self):
        return self.employee.first_name

    def get_employee_phone(self):
        return self.employee.get_phone()