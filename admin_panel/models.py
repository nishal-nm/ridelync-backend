from django.db import models
from django.contrib import admin


# Create your models here.
class CameraLocation(models.Model):
    cam_id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=255)

    class Meta:
        db_table = "CAM_LOC"  # Map to existing database table
        managed = False  # Prevent Django from modifying the table

    def __str__(self):
        return f"Camera {self.cam_id} - {self.location}"

class OwnerDetails(models.Model):
    vehicle_number = models.CharField(max_length=20, primary_key=True)  # Primary Key
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        db_table = "OWNER_DETAILS"  # Link to the existing table
        managed = False  # Django won't modify the table

    def __str__(self):
        return f"{self.vehicle_number} - {self.name}"