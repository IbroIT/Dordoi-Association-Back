### api/about-us/leadership

1. get all the data

```
http
api/about-us/leaders
```

result

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "photo": "http://localhost:8000/media/leaders/ivan_ivanov.jpg",
      "name": "Иван Иванов",
      "position": "Президент",
      "bio": "Краткое описание биографии Иван Иванов.",
      "achievements": [
        "Развитие программ поддержки",
        "Реализация международных проектов"
      ],
      "education": ["КНУ, 2000-2004", "Магистратура по управлению, 2005-2007"]
    },
    {
      "id": 2,
      "photo": "http://localhost:8000/media/leaders/aybek_alykov.jpg",
      "name": "Айбек Алымов",
      "position": "Исполнительный директор",
      "bio": "Краткое описание биографии Айбека Алымова.",
      "achievements": ["Увеличение охвата программ", "Оптимизация процессов"],
      "education": ["БГУ, 2005-2009"]
    }
  ]
}
```

2. get detailed one

```
http
api/about-us/leaders/<int:id>/
```

result

```json
{
  "id": 1,
  "photo": "http://localhost:8000/media/leaders/ivan_ivanov.jpg",
  "name": "Иван Иванов",
  "position": "Президент",
  "bio": "Полная биография Иван Иванов, в которой он делится опытом и достижениями, включает достижения в области международного сотрудничества и развития программ.",
  "achievements": [
    "Развитие программ поддержки",
    "Реализация международных проектов"
  ],
  "education": ["КНУ, 2000-2004", "Магистратура по управлению, 2005-2007"]
}
```

### api/partners

1. get all the data

```
http
api/partners
```

result

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 10,
      "logo": "http://localhost:8000/media/partners/logos/dordoi_logo.png",
      "name": "ТОО 'Dordoi Corporation'",
      "description": "Краткое описание компании Dordoi.",
      "otrasl": "Розничная торговля",
      "founded_year": 1993,
      "shtab_kvartira": "г. Бишкек, Кыргызстан",
      "about_company": "Подробная информация о компании Dordoi.",
      "ulugi": ["Оптовая торговля", "Розничная сеть"],
      "achievements": ["Лидер рынка", "Сертификаты качества"],
      "about_corporation": "Информация о вариантах сотрудничества.",
      "website": "https://dordoi.kg",
      "partnership_status": "Партнёр",
      "features": ["Широкая сеть", "Надёжность"]
    }
  ]
}
```

2. get detailed one

```
http
api/partners/<int:id>/
```

result

```json
{
  "id": 10,
  "logo": "http://localhost:8000/media/partners/logos/dordoi_logo.png",
  "name": "ТОО 'Dordoi Corporation'",
  "description": "Краткое описание компании Dordoi.",
  "otrasl": "Розничная торговля",
  "founded_year": 1993,
  "shtab_kvartira": "г. Бишкек, Кыргызстан",
  "about_company": "Подробная информация о компании Dordoi.",
  "ulugi": ["Оптовая торговля", "Розничная сеть"],
  "achievements": ["Лидер рынка", "Сертификаты качества"],
  "about_corporation": "Информация о вариантах сотрудничества.",
  "website": "https://dordoi.kg",
  "partnership_status": "Партнёр",
  "features": ["Широкая сеть", "Надёжность"]
}
```
