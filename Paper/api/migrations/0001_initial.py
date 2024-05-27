# Generated by Django 5.0.6 on 2024-05-15 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permission_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('hassed_password', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('adress', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('itemLocation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
        migrations.CreateModel(
            name='TwoFactorAuthentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
                ('verification_code', models.CharField(max_length=100)),
                ('expired', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordReset',
            fields=[
                ('token_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=100)),
                ('expired', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionRole',
            fields=[
                ('permission_role_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
            ],
            options={
                'unique_together': {('permission', 'role')},
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('user_role_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
            ],
            options={
                'unique_together': {('user', 'role')},
            },
        ),
    ]
