# Generated by Django 4.1.6 on 2023-02-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_alter_profiles_ciity_alter_profiles_paired_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Paired_with',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]
