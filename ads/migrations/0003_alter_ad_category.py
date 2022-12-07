from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ads.category'),
        ),
    ]
