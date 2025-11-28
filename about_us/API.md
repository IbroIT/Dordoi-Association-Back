# About Us API Documentation

## 📋 Endpoints

### 1. **Получить все факт-карты**

```
GET /api/about-us/facts/?lang=ru
```

**Query Parameters:**

- `lang` - язык (en, ru, kg) - по умолчанию `ru`
- `search` - поиск по названию и описанию
- `ordering` - сортировка (id, title_ru, title_en, title_kg)

**Response:**

```json
{
  "count": 5,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "icon": "http://localhost:8000/media/fact_cards/icon.png",
      "title": "Наша миссия",
      "description": "Мы стремимся к развитию образования...",
      "details": [
        {
          "id": 1,
          "detail": "Деталь 1"
        },
        {
          "id": 2,
          "detail": "Деталь 2"
        }
      ]
    }
  ]
}
```

### 2. **Получить детали фактов**

```
GET /api/about-us/details/?lang=ru&card=1
```

**Query Parameters:**

- `lang` - язык (en, ru, kg) - по умолчанию `ru`
- `card` - ID факт-карты (фильтр)
- `ordering` - сортировка (id, card)

**Response:**

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "detail": "Деталь 1"
    },
    {
      "id": 2,
      "detail": "Деталь 2"
    }
  ]
}
```

---

## 📝 FactCard модель

**Поля:**

- `id` - уникальный идентификатор (readonly)
- `icon` - изображение иконки
- `title` - заголовок на текущем языке
- `description` - описание на текущем языке
- `details` - массив связанных деталей

**Локализованные поля в БД:**

- `title_en`, `title_ru`, `title_kg`
- `description_en`, `description_ru`, `description_kg`

---

## ✨ Особенности

1. **Многоязычность** - параметр `?lang=ru/en/kg` определяет язык ответа
2. **Автоматический fallback** - если перевод на выбранный язык не доступен, будет использован русский, потом английский
3. **Вложенные данные** - факт-карты включают все связанные детали
4. **Оптимизация БД** - используется `prefetch_related` и `select_related`
5. **Поиск** - поддерживает поиск по названию и описанию на всех языках

---

## 🔗 Пример использования в React

```javascript
import { useState, useEffect } from "react";

const API_BASE_URL = "http://localhost:8000/api/about-us";

const AboutFacts = () => {
  const [facts, setFacts] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchFacts = async () => {
      try {
        setLoading(true);
        const lang = localStorage.getItem("i18nextLng") || "ru";
        const response = await fetch(`${API_BASE_URL}/facts/?lang=${lang}`);
        const data = await response.json();
        setFacts(data.results);
      } catch (error) {
        console.error("Error fetching facts:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchFacts();
  }, []);

  if (loading) return <div>Loading...</div>;

  return (
    <div>
      {facts.map((fact) => (
        <div key={fact.id}>
          <img src={fact.icon} alt={fact.title} />
          <h3>{fact.title}</h3>
          <p>{fact.description}</p>
          <ul>
            {fact.details.map((detail) => (
              <li key={detail.id}>{detail.detail}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default AboutFacts;
```

---

## 📦 Создание миграции

После добавления модели, выполните:

```bash
python manage.py makemigrations about_us
python manage.py migrate
```

---

**Готово к использованию! 🎉**
