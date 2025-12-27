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

**Query Parameters:**
- `lang`: Язык ответа (ru, en, kg). По умолчанию ru.