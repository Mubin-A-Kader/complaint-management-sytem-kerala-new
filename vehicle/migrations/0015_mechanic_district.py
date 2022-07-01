# Generated by Django 4.0.5 on 2022-07-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0014_remove_mechanic2_salary_mechanic2_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='district',
            field=models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Wayanad', 'Wayanad'), ('Ernakulam', 'Ernakulam'), ('Thrissur', 'Thrissur'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Pathanamthitta', 'Pathanamthitta'), ('Palakkad', 'Palakkad'), ('Malappuram', 'Malappuram'), ('Kozhikode', 'Kozhikode'), ('Kottayam', 'Kottayam'), ('Kollam', 'Kollam'), ('Kasaragod', 'Kasaragod'), ('Kannur', 'Kannur'), ('Idukki', 'Idukki')], default='Alappuzha', max_length=50),
            preserve_default=False,
        ),
    ]