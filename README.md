# Telegram Lead-Generation Quiz Bot

[English](#english) | [Українська](#українська) | [Русский](#русский)

---

## English

A lightweight, asynchronous Telegram lead-generation quiz bot built with **Python 3.11+**, **aiogram 3.x**, and in-memory Finite State Machine (FSM) storage. Designed for fast deployment without external database dependencies.

### Features
- **Interactive 3-Step Quiz**: Guides prospects through selecting a service (`Website`, `Telegram Bot`, `Automation`), specifying an approximate budget (`$100–$300`, `$300–$700`, `$700+`), and providing contact details.
- **Contact Verification & Validation**: Supports one-tap native Telegram phone number sharing (with sender ownership verification) as well as regex-validated manual input for phone numbers and `@username` handles.
- **Instant Admin Notifications**: Formats and forwards completed leads directly to a designated `ADMIN_CHAT_ID` using safe HTML escaping and clickable profile links.
- **Zero-Database Architecture**: Uses `MemoryStorage` for state management, keeping the footprint minimal and deployment straightforward.

### Tech Stack
- **Language**: Python 3.11+
- **Framework**: `aiogram` (`>=3.7,<4.0`)
- **Configuration**: `python-dotenv` (`>=1.0,<2.0`)

### Project Structure
```text
├── main.py            # Bot entry point, FSM states, handlers, and validation logic
├── config.py          # Environment variable loading and validation
├── requirements.txt   # Project dependencies
├── .env.example       # Template for environment variables
└── README.md          # Project documentation
```

### Installation & Setup

1. **Clone the repository and navigate to the project folder:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   ```
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Copy `.env.example` to `.env` and fill in your credentials:
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   ADMIN_CHAT_ID=123456789
   ```
   > **Note:** Make sure you have started a chat with the bot from your admin account (or added the bot to the target admin group) so it has permission to send messages to `ADMIN_CHAT_ID`.

5. **Run the bot:**
   ```bash
   python main.py
   ```

### Notes
- Quiz states are stored in RAM (`MemoryStorage`) and will reset if the bot process restarts.
- To customize services or budget tiers, edit `SERVICE_OPTIONS`, `BUDGET_OPTIONS`, and their corresponding keyboard builders in `main.py`.

---

## Українська

Легкий асинхронний Telegram-бот для генерації лідів у форматі квізу, створений на **Python 3.11+**, **aiogram 3.x** та вбудованому сховищі станів (FSM) у пам'яті. Розроблений для швидкого розгортання без необхідності підключення зовнішніх баз даних.

### Основні можливості
- **Інтерактивний квіз із 3 кроків**: Проводить клієнта через вибір послуги (`Website`, `Telegram Bot`, `Automation`), орієнтовного бюджету (`$100–$300`, `$300–$700`, `$700+`) та передачу контактних даних.
- **Валідація та перевірка контактів**: Підтримує надсилання номера телефону в один дотик через стандартну кнопку Telegram (із перевіркою належності номера відправнику), а також ручне введення телефону або `@username` із перевіркою через регулярні вирази.
- **Миттєві сповіщення адміністратора**: Форматує та надсилає готові заявки безпосередньо вказаному отримувачу (`ADMIN_CHAT_ID`) з безпечним екрануванням HTML та прямим посиланням на профіль клієнта.
- **Архітектура без бази даних**: Використовує `MemoryStorage` для керування станами діалогу, що забезпечує мінімальне навантаження та простий запуск.

### Технологічний стек
- **Мова**: Python 3.11+
- **Фреймворк**: `aiogram` (`>=3.7,<4.0`)
- **Конфігурація**: `python-dotenv` (`>=1.0,<2.0`)

### Структура проєкту
```text
├── main.py            # Точка входу, стани FSM, обробники подій та валідація
├── config.py          # Завантаження та перевірка змінних оточення
├── requirements.txt   # Залежності проєкту
├── .env.example       # Шаблон файлу змінних оточення
└── README.md          # Документація проєкту
```

### Встановлення та запуск

1. **Клонуйте репозиторій та перейдіть у директорію проєкту:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Створіть та активуйте віртуальне середовище:**
   ```bash
   python -m venv .venv
   ```
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Встановіть залежності:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Налаштуйте змінні оточення:**
   Скопіюйте `.env.example` у `.env` та вкажіть свої дані:
   ```bash
   cp .env.example .env
   ```
   Вміст `.env`:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   ADMIN_CHAT_ID=123456789
   ```
   > **Примітка:** Переконайтеся, що ви активували діалог із ботом з акаунту адміністратора (або додали бота до відповідного чату), щоб він мав право надсилати повідомлення на `ADMIN_CHAT_ID`.

5. **Запустіть бота:**
   ```bash
   python main.py
   ```

### Примітки
- Проміжний прогрес користувачів зберігається в оперативній пам'яті (`MemoryStorage`) і скидається під час перезапуску бота.
- Щоб змінити перелік послуг або варіанти бюджету, відредагуйте словники `SERVICE_OPTIONS`, `BUDGET_OPTIONS` та відповідні функції клавіатур у файлі `main.py`.

---

## Русский

Лёгкий асинхронный Telegram-бот для лидогенерации в формате квиза, написанный на **Python 3.11+**, **aiogram 3.x** и хранилище состояний (FSM) в оперативной памяти. Спроектирован для быстрого развёртывания без подключения внешних баз данных.

### Основные возможности
- **Интерактивный квиз из 3 шагов**: Проводит потенциального клиента через выбор услуги (`Website`, `Telegram Bot`, `Automation`), примерного бюджета (`$100–$300`, `$300–$700`, `$700+`) и отправку контактных данных.
- **Валидация и проверка контактов**: Поддерживает отправку номера телефона в одно нажатие через нативную кнопку Telegram (с проверкой принадлежности контакта отправителю), а также ручной ввод телефона или `@username` с проверкой по регулярным выражениям.
- **Мгновенные уведомления администратора**: Форматирует и отправляет готовые заявки напрямую в указанный `ADMIN_CHAT_ID` с безопасным экранированием HTML и ссылкой на профиль пользователя.
- **Архитектура без базы данных**: Использует `MemoryStorage` для хранения состояний диалога, что делает проект максимально лёгким и простым в запуске.

### Технологический стек
- **Язык**: Python 3.11+
- **Фреймворк**: `aiogram` (`>=3.7,<4.0`)
- **Конфигурация**: `python-dotenv` (`>=1.0,<2.0`)

### Структура проекта
```text
├── main.py            # Точка входа, состояния FSM, обработчики и валидация
├── config.py          # Загрузка и валидация переменных окружения
├── requirements.txt   # Зависимости проекта
├── .env.example       # Шаблон файла переменных окружения
└── README.md          # Документация проекта
```

### Установка и запуск

1. **Клонируйте репозиторий и перейдите в папку проекта:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Создайте и активируйте виртуальное окружение:**
   ```bash
   python -m venv .venv
   ```
   - **Windows (PowerShell):**
     ```powershell
     .\.venv\Scripts\Activate.ps1
     ```
   - **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```

3. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройте переменные окружения:**
   Скопируйте `.env.example` в `.env` и заполните своими данными:
   ```bash
   cp .env.example .env
   ```
   Содержимое `.env`:
   ```env
   BOT_TOKEN=your_telegram_bot_token
   ADMIN_CHAT_ID=123456789
   ```
   > **Примечание:** Убедитесь, что вы запустили бота с аккаунта администратора (или добавили бота в целевой админ-чат), чтобы у него были права на отправку сообщений в `ADMIN_CHAT_ID`.

5. **Запустите бота:**
   ```bash
   python main.py
   ```

### Примечания
- Промежуточный прогресс пользователей хранится в оперативной памяти (`MemoryStorage`) и сбрасывается при перезапуске процесса бота.
- Для изменения списка услуг или диапазонов бюджета отредактируйте словари `SERVICE_OPTIONS`, `BUDGET_OPTIONS` и соответствующие функции клавиатур в файле `main.py`.
