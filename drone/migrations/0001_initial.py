# Generated by Django 4.2.2 on 2023-06-07 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('max_speed', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Job',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Service Categories',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=20)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='user_profiles/')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.servicecategory')),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.drone')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.job')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.user')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=255)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.user')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.job')),
            ],
            options={
                'verbose_name': 'Proposal',
                'verbose_name_plural': 'Proposals',
            },
        ),
        migrations.AddField(
            model_name='job',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.user'),
        ),
        migrations.AddField(
            model_name='job',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.service'),
        ),
        migrations.AddField(
            model_name='drone',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drone.user'),
        ),
    ]
