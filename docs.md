# 1. баннеры
```http
api/banners
```

res
```json
[
	{
		"id": 1,
		"image": "https://bucketeer-8676b90e-ab51-4272-9cee-1824a2d6c0ea.s3-eu-west-1.amazonaws.com/partners/banners/banner.png",
		"title": "Тестовый баннер",
		"idea": "Возможность для роста",
		"desctip": "Короткое описание баннера",
		"link_url": "https://example.com"
	}
]
```

# 2. этот эндпоинт вернет все факты которые отмечены как banner
```http
api/about-us/fact_banners
``` 

res
```json
[
	{
		"id": 1,
		"icon": "https://bucketeer-8676b90e-ab51-4272-9cee-1824a2d6c0ea.s3-eu-west-1.amazonaws.com/fact_cards/fact-icon.png",
		"title": "Тестовый факт",
		"description": "Русское описание",
		"details": "Деталь RU",
		"is_banner": true
	}
]
```

# 3. возрощает все news которые отмечены как banner
```http
api/presscentre/news-banners
```

res
```json
[
	{
		"id": 1,
		"title": "Тестовая новость",
		"description": "Полное описание RU",
		"short_description": "Краткое описание RU",
		"image": "https://bucketeer-8676b90e-ab51-4272-9cee-1824a2d6c0ea.s3-eu-west-1.amazonaws.com/news/news.png",
		"is_recommended": true,
		"created_at": "2025-12-13T16:42:04.222589Z",
		"updated_at": "2025-12-13T16:42:05.413097Z",
		"published_at": "2025-12-13",
		"category": {
			"id": 1,
			"title": "Аналитика"
		},
		"is_banner": true
	}
]
```

# 4. галерея
```http
api/gallery/categories
```


res -- categories
```json
[
	{
		"id": 1,
		"name_en": "Culture",
		"name_kg": "Маданият",
		"name_ru": "Культура"
	}
]
```

```http
api/gallery/galleries
```

res -- galleries
```json
[
	{
		"id": 1,
		"title_en": "Gallery Title",
		"title_kg": "Галереянын аталышы",
		"title_ru": "Название галереи",
		"category": {
			"id": 1,
			"name_en": "Culture",
			"name_kg": "Маданият",
			"name_ru": "Культура"
		},
		"photos": [
			{
				"id": 1,
				"image": "https://bucketeer-8676b90e-ab51-4272-9cee-1824a2d6c0ea.s3-eu-west-1.amazonaws.com/gallery/gallery.png"
			}
		]
	}
]
```


# 5. контакты
```http
api/contacts
```

res
```json
[
	{
		"id": 1,
		"logo": "https://bucketeer-8676b90e-ab51-4272-9cee-1824a2d6c0ea.s3-eu-west-1.amazonaws.com/contacts/logos/contact.png",
		"name": "Dordoi Association",
		"email": "info@example.com",
		"phone": "+996700000000",
		"work_time": "Пн-Пт 09:00-18:00",
		"tg_link": "https://t.me/example",
		"wb_link": "https://wa.me/700000000",
		"ins_link": "https://instagram.com/example"
	}
]
```

