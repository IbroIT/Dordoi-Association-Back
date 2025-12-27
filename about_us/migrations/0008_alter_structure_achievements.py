# Generated manually to fix achievements fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("about_us", "0007_alter_structure_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="structure",
            name="achievements_en",
            field=models.JSONField(
                default=list,
                help_text="Список достижений на английском",
                verbose_name="Достижения (EN)",
            ),
        ),
        migrations.AlterField(
            model_name="structure",
            name="achievements_ru",
            field=models.JSONField(
                default=list,
                help_text="Список достижений на русском",
                verbose_name="Достижения (RU)",
            ),
        ),
        migrations.AlterField(
            model_name="structure",
            name="achievements_kg",
            field=models.JSONField(
                default=list,
                help_text="Список достижений на кыргызском",
                verbose_name="Достижения (KG)",
            ),
        ),
    ]