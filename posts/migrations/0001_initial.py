# Generated by Django 4.2.5 on 2023-09-30 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_users_secondlastname_alter_users_secondname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
