# Generated by Django 2.2.19 on 2021-05-04 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_emails', '0002_auto_20210403_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='SENDING',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='MessageSent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SEND_DATE', models.DateTimeField(auto_now=True)),
                ('MESSAGE', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_emails.Message')),
            ],
        ),
    ]
