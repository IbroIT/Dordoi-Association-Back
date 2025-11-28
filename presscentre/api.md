## news part

### categories

```http
/api/presscentre/categories/
```

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Категория RU"
        }
    ]
}
```

### 2 news

```http
/api/presscentre/news/
```

```json
{
  "id": 1,
  "title": "Заголовок (RU):",
  "description": "Описание (RU):",
  "short_description": "Краткое описание (RU):",
  "image": "http://127.0.0.1:8000/news/photo_2025-11-20_11-34-52.jpg",
  "is_recommended": true,
  "created_at": "2025-11-27T20:31:31.117839Z",
  "updated_at": "2025-11-27T20:31:31.117858Z",
  "category": {
    "id": 1,
    "title": "Категория RU"
  }
}
```
