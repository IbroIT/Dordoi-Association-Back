## about us facts

### full card

```http
/api/about-us/facts/?lang=ru
```

```json
{
    "count": 6,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "icon": "http://127.0.0.1:8000/fact_cards/forbes_icon.jpg",
            "title": "Включение в рейтинг Forbes Global 2000",
            "description": "Компания включена в престижный рейтинг Forbes Global 2000 крупнейших компаний мира",
            "details": [
                {
                    "id": 1,
                    "detail": "Включение в рейтинг Forbes Global 2000"
                },
                {
                    "id": 2,
                    "detail": "Признание среди топ-компаний мира"
                }
            ]
        },
        {
            "id": 2,
            "icon": "http://127.0.0.1:8000/fact_cards/smokeless_icon.jpg",
            "title": "Безопасное производство",
            "description": "15% снижение вредных выбросов благодаря современным технологиям",
            "details": [
                {
                    "id": 3,
                    "detail": "Внедрение экологически чистых технологий"
                }
            ]
        }
    ]
}
```

### detail card

```http
/api/about-us/details/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "detail": "Включение в рейтинг Forbes Global 2000"
        }
    ]
}
```

## about us history

### history list

```http
/api/about-us/history/
```

```json
{
        "id": 1,
        "description": "adfesfagsdfadgshd",
        "image": "http://127.0.0.1:8000/media/history/d7d4704ee1caa586fc73c71ea47d7041.jpg",
        "order": 0
}
```

## about us stucture 
### Structure List
```json
/api/about-us/structure/
```

```json
 {
        "id": 2,
        "slug": "dordoi-logistics",
        "logo": "http://127.0.0.1:8000/media/subsidiaries/logos/https___promoname.ru_wp-content_uploads_2023_08_photo_421-31-10-2021_22-04-32.jpg",
        "name": "AKTAN KASHYMBEKOV",
        "short_description": "dsafasdfasdasdfsadfasd",
        "description": "asdfsad",
        "founded_year": 1222,
        "achievements": [
            "lg"
        ],
        "address": "Bishkek",
        "email": "aktam200e@gmail.com",
        "phone": "55555",
        "website": "http://127.0.0.1:8000/admin/student_clubs/exchangeprogram/add/",
        "order": 0
    },
    {
        "id": 1,
        "slug": "dordoi-trade",
        "logo": "http://127.0.0.1:8000/media/subsidiaries/logos/photo_2025-11-20_11-34-52.jpg",
        "name": "AKTAN KASHYMBEKOV",
        "short_description": "afweawefaewf",
        "description": "fdasghjk",
        "founded_year": 2003,
        "achievements": [
            "dawdawd"
        ],
        "address": "Bishkek",
        "email": "aktam200e@gmail.com",
        "phone": "55555",
        "website": "http://127.0.0.1:8000/admin/student_clubs/exchangeprogram/add/",
        "order": 1
    }
```

### Structure Instance ПРИМЕР
```http
/api/about-us/structure/dordoi-logistics/
```

```json
{
    "id": 2,
    "slug": "dordoi-logistics",
    "logo": "http://127.0.0.1:8000/media/subsidiaries/logos/https___promoname.ru_wp-content_uploads_2023_08_photo_421-31-10-2021_22-04-32.jpg",
    "name": "AKTAN KASHYMBEKOV",
    "short_description": "dsafasdfasdasdfsadfasd",
    "description": "asdfsad",
    "founded_year": 1222,
    "achievements": [
        "lg"
    ],
    "address": "Bishkek",
    "email": "aktam200e@gmail.com",
    "phone": "55555",
    "website": "http://127.0.0.1:8000/admin/student_clubs/exchangeprogram/add/",
    "order": 0
}
```
