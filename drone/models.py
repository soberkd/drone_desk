from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    profile_image = models.ImageField(
        upload_to='user_profiles/', blank=True, null=True)

    # Add other user-related fields as needed

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Drone(models.Model):
    name = models.CharField(max_length=255)
    operator = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    max_speed = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    # Add other drone-related fields as needed


class ServiceCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    # Add other job-related fields as needed

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"

    def __str__(self):
        return self.title


class Proposal(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=255)
    # Add other proposal-related fields as needed

    class Meta:
        verbose_name = "Proposal"
        verbose_name_plural = "Proposals"

    def __str__(self):
        return f"Proposal for {self.job.title} by {self.bidder.username}"


class Review(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f"Review for {self.job.title} by {self.reviewer.username}"
