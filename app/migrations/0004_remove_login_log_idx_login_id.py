# Generated by Django 4.1 on 2022-10-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_login"),
    ]

    operations = [
        migrations.RemoveField(model_name="login", name="log_idx",),
        migrations.AddField(
            model_name="login",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
