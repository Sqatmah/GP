# from django.db import models
# from django.contrib.auth.models import User
# from customer.models import Customer




# class PolicyRecord(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     Policy= models.ForeignKey(Policy, on_delete=models.CASCADE)
#     status = models.CharField(max_length=100,default='Pending')
#     creation_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.policy

# class Question(models.Model):
#     customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
#     description =models.CharField(max_length=500)
#     admin_comment=models.CharField(max_length=200,default='Nothing')
#     asked_date =models.DateField(auto_now=True)
#     def __str__(self):
#         return self.description