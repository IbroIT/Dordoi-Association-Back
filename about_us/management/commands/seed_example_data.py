from django.core.management.base import BaseCommand
from django.apps import apps


class Command(BaseCommand):
    help = "Seed example leaders and partners data (idempotent)"

    def handle(self, *args, **options):
        # Fetch models
        Leader = apps.get_model("about_us", "Leader")
        Partner = None
        if apps.is_installed("partners"):
            try:
                Partner = apps.get_model("partners", "Partner")
            except LookupError:
                Partner = None

        # Leaders sample data
        leaders = [
            {
                "name_ru": "Иван Иванов",
                "name_en": "Ivan Ivanov",
                "name_kg": "Иван Иванов",
                "position_ru": "Президент",
                "position_en": "President",
                "position_kg": "Президент",
                "bio_ru": "Полная биография Иван Иванов, опытный руководитель и организатор международных проектов.",
                "bio_en": "Full biography of Ivan Ivanov, an experienced leader and organizer of international projects.",
                "bio_kg": "Толук биография Иван Иванов.",
                "achievements_ru": [
                    "Развитие программ поддержки",
                    "Реализация международных проектов",
                ],
                "achievements_en": [
                    "Developed support programs",
                    "Executed international projects",
                ],
                "achievements_kg": ["Жетишкендик 1", "Жетишкендик 2"],
                "education_ru": ["КНУ, 2000-2004", "Магистратура по управлению, 2005-2007"],
                "education_en": ["KNU, 2000-2004", "Master in Management, 2005-2007"],
                "education_kg": ["Билим 1"],
                "photo": "leaders/ivan_ivanov.jpg",
            },
            {
                "name_ru": "Айбек Алымов",
                "name_en": "Aibek Alimov",
                "name_kg": "Айбек Алымов",
                "position_ru": "Исполнительный директор",
                "position_en": "Executive Director",
                "position_kg": "Исполнительный директор",
                "bio_ru": "Короткое описание биографии Айбека Алымова.",
                "bio_en": "Short bio of Aibek Alimov.",
                "bio_kg": "Айбек жөнүндө кыскача маалымат.",
                "achievements_ru": ["Увеличение охвата программ", "Оптимизация процессов"],
                "achievements_en": ["Expanded program reach", "Process optimization"],
                "achievements_kg": ["Жетишкендик 3"],
                "education_ru": ["БГУ, 2005-2009"],
                "education_en": ["BSU, 2005-2009"],
                "education_kg": ["Билим 2"],
                "photo": "leaders/aybek_alykov.jpg",
            },
        ]

        for data in leaders:
            name_ru = data.get("name_ru")
            defaults = data.copy()
            # idempotent: update or create based on name_ru
            obj, created = Leader.objects.update_or_create(name_ru=name_ru, defaults=defaults)
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action} Leader: {obj.name_ru} (id={obj.id})"))

        # Partners sample data (skip if app is not installed)
        if Partner is None:
            self.stdout.write(self.style.WARNING("Partners app is not installed or Partner model not available. Skipping partners seeding."))
            return

        partners = [
            {
                "logo": "partners/logos/dordoi_logo.png",
                "name_ru": "ТОО 'Dordoi Corporation'",
                "name_en": "Dordoi Corporation",
                "name_kg": "Dordoi Corporation",
                "description_ru": "Краткое описание компании Dordoi.",
                "description_en": "Brief description of Dordoi Corporation.",
                "description_kg": "Dordoi корпорация жөнүндө кыскача маалымат.",
                "otrasl_ru": "Розничная торговля",
                "otrasl_en": "Retail",
                "otrasl_kg": "Чакан жана ири соода",
                "founded_year": 1993,
                "shtab_kvartira_ru": "г. Бишкек, Кыргызстан",
                "shtab_kvartira_en": "Bishkek, Kyrgyzstan",
                "shtab_kvartira_kg": "Бишкек, Кыргыз Республикасы",
                "about_company_ru": "Подробная информация о компании Dordoi.",
                "about_company_en": "Detailed information about Dordoi Corporation.",
                "about_company_kg": "Dordoi компаниясы жөнүндө толук маалымат.",
                "ulugi_ru": ["Оптовая торговля", "Розничная сеть"],
                "ulugi_en": ["Wholesale", "Retail network"],
                "ulugi_kg": ["Оптовая соода", "Чакан соода"],
                "achievements_ru": ["Лидер рынка", "Сертификаты качества"],
                "achievements_en": ["Market leader", "Quality certifications"],
                "achievements_kg": ["Нарыкта лидер", "Сапат күбөлүктөрү"],
                "about_corporation_ru": "Информация о вариантах сотрудничества.",
                "about_corporation_en": "Information about partnership opportunities.",
                "about_corporation_kg": "Өнөктөштүктүн мүмкүнчүлүктөрү жөнүндө маалымат.",
                "website": "https://dordoi.kg",
                "partnership_status_ru": "Партнёр",
                "partnership_status_en": "Partner",
                "partnership_status_kg": "Өнөктөш",
                "features_ru": ["Широкая сеть", "Надёжность"],
                "features_en": ["Wide network", "Reliability"],
                "features_kg": ["Кең тармак", "Ишенимдүүлүк"],
            }
        ]

        for data in partners:
            name_ru = data.get("name_ru")
            defaults = data.copy()
            obj, created = Partner.objects.update_or_create(name_ru=name_ru, defaults=defaults)
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action} Partner: {obj.name_ru} (id={obj.id})"))
