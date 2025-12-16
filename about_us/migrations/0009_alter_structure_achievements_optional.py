# Generated manually to make achievements fields optional

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_us", "0008_alter_structure_achievements"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structure",
            name="achievements_en",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="Список достижений на английском",
                null=True,
                verbose_name="Достижения (EN)",
            ),
        ),
        migrations.AlterField(
            model_name="structure",
            name="achievements_ru",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="Список достижений на русском",
                null=True,
                verbose_name="Достижения (RU)",
            ),
        ),
        migrations.AlterField(
            model_name="structure",
            name="achievements_kg",
            field=models.JSONField(
                blank=True,
                default=list,
                help_text="Список достижений на кыргызском",
                null=True,
                verbose_name="Достижения (KG)",
            ),
        ),
    ]