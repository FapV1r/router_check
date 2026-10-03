# Карта проекта Axlerator (SmartDorm)

## Обзор проекта

**SmartDorm** — система мониторинга и управления общежитием с использованием IoT-датчиков, машинного обучения для прогнозирования и обнаружения аномалий.

**Технологический стек:**
- **Backend:** FastAPI (Python)
- **База данных:** SQLite (файл `data/smartdorm.db`)
- **ORM:** SQLAlchemy
- **ML:** Модуль для обучения и прогнозирования (в разработке)
- **Frontend:** HTML-шаблоны (Jinja2)

---

## Структура директорий

```
Axlerator_progect/
├── app/                      # Основное приложение FastAPI
│   ├── routers/              # API-эндпоинты
│   │   ├── sensors.py        # CRUD для датчиков
│   │   ├── readings.py       # Запись показаний датчиков
│   │   ├── buildings.py      # Управление зданиями (пусто)
│   │   ├── alerts.py         # Управление алертами (пусто)
│   │   └── maintenance.py    # Управление заявками (пусто)
│   ├── services/             # Бизнес-логика и сервисы
│   │   ├── forcasting.py     # Прогнозирование (пусто)
│   │   ├── anomaly_detecter.py # Обнаружение аномалий (пусто)
│   │   └── simulator.py      # Симулятор данных (пусто)
│   ├── templates/            # HTML-шаблоны
│   │   ├── dashboard.html    # Главная панель (пусто)
│   │   ├── building.html     # Страница здания (пусто)
│   │   └── alerts.html       # Страница алертов (пусто)
│   ├── main.py               # Точка входа FastAPI
│   ├── models.py             # SQLAlchemy модели
│   ├── schemas.py            # Pydantic схемы
│   ├── database.py           # Конфигурация БД
│   ├── seed.py               # Начальные данные
│   └── test_hierarchy.py     # Тесты иерархии
├── data/                     # Данные
│   └── smartdorm.db          # SQLite база данных
├── ml/                       # Машинное обучение
│   ├── train.py              # Обучение моделей (пусто)
│   ├── predict.py            # Предсказания (пусто)
│   └── models/               # Сохранённые модели
├── simulator/                # Генератор тестовых данных
│   └── generate_data.py      # Генерация данных (пусто)
├── README.md                 # Документация (пусто)
└── requirement.txt           # Зависимости (пусто)
```

---

## Модели данных (models.py)

### Иерархия локаций

```
Location (здание/этаж/комната)
    └── parent_id → самореференс для построения дерева
    └── children → дочерние локации
```

### Основные сущности

| Модель | Описание | Ключевые поля |
|--------|----------|---------------|
| **Location** | Иерархическая локация (здание → этаж → комната) | `type`, `name`, `parent_id` |
| **Building** | Здание | `location_id`, `address` |
| **Floor** | Этаж | `location_id`, `number` |
| **Room** | Комната | `location_id`, `number`, `capacity` |
| **Sensor** | IoT-датчик | `location_id`, `type`, `name`, `unit`, `is_active` |
| **Reading** | Показания датчика | `sensor_id`, `value`, `timestamp` |
| **Alert** | Аварийное уведомление | `sensor_id`, `type`, `severity`, `probability`, `status` |
| **MaintenanceTicket** | Заявка на обслуживание | `sensor_id`, `description`, `status`, `created_at` |
| **User** | Пользователь системы | `username`, `email`, `role` |

---

## API-эндпоинты

### Реализованные

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| `GET` | `/` | Корневой эндпоинт, возвращает `{"message": "SmartDorm"}` |
| `GET` | `/sensors` | Список всех датчиков |
| `GET` | `/sensors/{sensor_id}` | Получить датчик по ID |
| `POST` | `/readings` | Создать запись показаний датчика |

### В разработке (пустые файлы)

- `/buildings/*` — управление зданиями
- `/alerts/*` — управление алертами
- `/maintenance/*` — управление заявками

---

## Текущее состояние проекта

### ✅ Реализовано

1. **Базовая структура FastAPI приложения**
2. **Модели данных SQLAlchemy** — полная схема БД
3. **Иерархическая система локаций** — здание → этаж → комната
4. **CRUD для датчиков** — получение списка и отдельных записей
5. **Запись показаний датчиков** — создание readings
6. **Seed-скрипт** — заполнение тестовыми данными

### 🚧 В разработке (пустые файлы)

1. **ML-модуль** (`ml/train.py`, `ml/predict.py`)
2. **Обнаружение аномалий** (`app/services/anomaly_detecter.py`)
3. **Прогнозирование** (`app/services/forcasting.py`)
4. **Симулятор данных** (`app/services/simulator.py`, `simulator/generate_data.py`)
5. **Frontend-шаблоны** (все HTML файлы пустые)
6. **Роутеры зданий, алертов, обслуживания**
7. **Документация и зависимости** (`README.md`, `requirement.txt`)

---

## Запуск проекта

### Установка зависимостей

```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

### Инициализация БД и заполнение тестовыми данными

```bash
cd Axlerator_progect
python -m app.seed
```

### Запуск сервера

```bash
cd Axlerator_progect
uvicorn app.main:app --reload
```

### Проверка API

```bash
curl http://localhost:8000/
curl http://localhost:8000/sensors
```

---

## Следующие шаги для развития

1. **Добавить requirements.txt** с актуальными зависимостями
2. **Реализовать ML-модуль** для прогнозирования потребления ресурсов
3. **Разработать систему алертов** с уведомлениями
4. **Создать веб-интерфейс** (dashboard) для мониторинга
5. **Добавить аутентификацию** (User модель уже есть)
6. **Реализовать симулятор** для генерации тестовых данных
7. **Написать тесты** для критических компонентов

---

## Пример использования API

### Создание показания датчика

```bash
curl -X POST http://localhost:8000/readings \
  -H "Content-Type: application/json" \
  -d '{"sensor_id": 1, "value": 23.5}'
```

### Получение списка датчиков

```bash
curl http://localhost:8000/sensors
```

Ответ:
```json
[
  {
    "id": 1,
    "name": "Temp 1_4_417",
    "type": "temperature",
    "location_id": 4,
    "unit": "C°",
    "is_active": true
  }
]
```

---

## Архитектура

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Application                   │
├─────────────────────────────────────────────────────────┤
│  Routers (API endpoints)                                │
│  ├── sensors.py ──── GET /sensors, GET /sensors/{id}   │
│  └── readings.py ─── POST /readings                     │
├─────────────────────────────────────────────────────────┤
│  Services (Business Logic)                              │
│  ├── forcasting.py (TODO)                               │
│  ├── anomaly_detecter.py (TODO)                         │
│  └── simulator.py (TODO)                                │
├─────────────────────────────────────────────────────────┤
│  Models (SQLAlchemy)                                    │
│  ├── Location, Building, Floor, Room                    │
│  ├── Sensor, Reading, Alert                             │
│  ├── MaintenanceTicket, User                            │
├─────────────────────────────────────────────────────────┤
│  Database: SQLite (data/smartdorm.db)                   │
└─────────────────────────────────────────────────────────┘
```

---

*Карта создана: 2026-09-03*
