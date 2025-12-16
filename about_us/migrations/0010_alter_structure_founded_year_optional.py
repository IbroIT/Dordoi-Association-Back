# Generated manually to make founded_year optional

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_us", "0009_alter_structure_achievements_optional"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structure",
            name="founded_year",
            field=models.IntegerField(
                blank=True,
                null=True,
                verbose_name="Год основания",
            ),
        ),
    ]
