from django.db import models

# Create your models here.
class info(models.Model):

    male = models.IntegerField(null=False)
    BPMeds = models.IntegerField(default=0) #Có sử dụng thuốc hạ huyết áp không, có hoặc không
    prevalentStroke = models.IntegerField(default=0) #Đột quỵ phổ biến, có hoặc không
    prevalentHyp = models.IntegerField(default=0) #Tăng huyết áp phổ biến, có hoặc không
    diabetes = models.IntegerField(default=0) #Có bị đái tháo đường hay không
    log_cigsPerDay = models.IntegerField(default=0) #Số điếu thuốc hút 1 ngày
    log_totChol = models.FloatField(null=False) #Tổng lượng Cholesteron
    log_diaBP = models.FloatField(null=False) #huyết áp tâm trương
    log_BMI = models.FloatField(null=False) #Chỉ số BMI
    log_heartRate = models.FloatField(null=False) #Nhịp tim đập mỗi phút
    log_glucose = models.FloatField(null=False) #Lượng glucoso trong máu
    log_age = models.IntegerField(null=False) #Tuổi

    def __str__(self):
        return self.name