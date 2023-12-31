# Generated by Django 4.2.5 on 2023-10-05 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_permission_rename_description_role_role_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='role',
            new_name='role_user',
        ),
        migrations.AddField(
            model_name='role',
            name='role_permission',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.permission'),
            preserve_default=False,
        ),
    ]
