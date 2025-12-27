from django.core.management.base import BaseCommand
from about_us.models import FactCard, FactDetail, Leader
from partners.models import Partner
from presscentre.models import Category, News
from django.core.files.base import ContentFile
import os


class Command(BaseCommand):
    help = 'Load sample data for testing'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create FactCard
        fact_card = FactCard.objects.create(
            title_en="Our History",
            title_ru="Наша история",
            title_kg="Биздин тарыхыбыз",
            description_en="Learn about our organization's history and achievements",
            description_ru="Узнайте о истории и достижениях нашей организации",
            description_kg="Уюмубуздун тарыхы жана жетишкендиктери жөнүндө билүү"
        )
        # Create a dummy image file for the icon
        fact_card.icon.save('default_icon.png', ContentFile(b'dummy image data'))
        self.stdout.write(f'Created FactCard: {fact_card}')

        # Create FactDetail
        fact_detail = FactDetail.objects.create(
            card=fact_card,
            detail_en="Founded in 1990",
            detail_ru="Основан в 1990 году",
            detail_kg="1990-жылы негизделген"
        )
        self.stdout.write(f'Created FactDetail: {fact_detail}')

        # Create Leader
        leader = Leader.objects.create(
            name_en="John Smith",
            name_ru="Джон Смит",
            name_kg="Джон Смит",
            position_en="Executive Director",
            position_ru="Исполнительный директор",
            position_kg="Аткаруучу директор",
            bio_en="Experienced leader with 20+ years in the industry",
            bio_ru="Опытный лидер с более чем 20-летним опытом в отрасли",
            bio_kg="Орто 20 жылдан ашуун тажрыйбасы бар тажрыйбалуу лидер",
            achievements_en=["Award 1", "Award 2"],
            achievements_ru=["Награда 1", "Награда 2"],
            achievements_kg=["Сыйлык 1", "Сыйлык 2"],
            education_en=["MBA", "PhD"],
            education_ru=["MBA", "PhD"],
            education_kg=["MBA", "PhD"]
        )
        # Create a dummy image file for the photo
        leader.photo.save('default_photo.png', ContentFile(b'dummy image data'))
        self.stdout.write(f'Created Leader: {leader}')

        # Create Partner
        partner = Partner.objects.create(
            name_en="Tech Corp",
            name_ru="Тех Корп",
            name_kg="Тех Корп",
            description_en="Leading technology company",
            description_ru="Ведущая технологическая компания",
            description_kg="Алдыңкы технологиялык компания",
            otrasl_en="Technology",
            otrasl_ru="Технологии",
            otrasl_kg="Технология",
            founded_year=2000,
            shtab_kvartira_en="New York, USA",
            shtab_kvartira_ru="Нью-Йорк, США",
            shtab_kvartira_kg="Нью-Йорк, АКШ",
            about_company_en="About our company",
            about_company_ru="О нашей компании",
            about_company_kg="Биздин компания жөнүндө",
            ulugi_en=["Service 1", "Service 2"],
            ulugi_ru=["Услуга 1", "Услуга 2"],
            ulugi_kg=["Кызмат 1", "Кызмат 2"],
            achievements_en=["Achievement 1"],
            achievements_ru=["Достижение 1"],
            achievements_kg=["Жетишкендик 1"],
            about_corporation_en="About partnership",
            about_corporation_ru="О партнерстве",
            about_corporation_kg="Өнөктөштүк жөнүндө",
            website="https://example.com",
            partnership_status_en="Active",
            partnership_status_ru="Активный",
            partnership_status_kg="Активдүү",
            features_en=["Feature 1"],
            features_ru=["Преимущество 1"],
            features_kg=["Артыкчылык 1"]
        )
        # Create a dummy image file for the logo
        partner.logo.save('default_logo.png', ContentFile(b'dummy image data'))
        self.stdout.write(f'Created Partner: {partner}')

        # Create Category
        category = Category.objects.create(
            title_en="News",
            title_ru="Новости",
            title_kg="Жаңылыктар"
        )
        self.stdout.write(f'Created Category: {category}')

        # Create News
        news = News.objects.create(
            category=category,
            is_recommended=True,
            title_en="Important Announcement",
            title_ru="Важное объявление",
            title_kg="Маанилүү жарыя",
            short_description_en="Short description",
            short_description_ru="Краткое описание",
            short_description_kg="Кыскача сүрөттөмө",
            fulltext_en="Full news text in English",
            fulltext_ru="Полный текст новости на русском",
            fulltext_kg="Жаңылыктын толук тексти кыргызча",
            published_date="2025-12-10"
        )
        self.stdout.write(f'Created News: {news}')

        self.stdout.write(self.style.SUCCESS('Successfully loaded sample data!'))