Бэкенд-приложение на FastAPI (Python) с возможностями:

Загрузка файлов (PDF, CSV, Excel)

AI-парсинг структуры таблиц с помощью pandas и pdfplumber

Преобразование данных в унифицированный формат

API для получения структурированных данных

Готово к деплою на Railway

datafabricx/
├── app/
│   ├── main.py              # Точка входа (FastAPI)
│   ├── parsers.py           # AI-парсинг PDF, Excel, CSV
│   ├── transformer.py       # Семантическая нормализация
│   └── models.py            # Модели API
├── requirements.txt
├── Procfile
├── README.md
└── .railway/ (автоматически создаётся при деплое)

frontend/
├── index.html
├── package.json
├── public/
├── src/
│   ├── App.jsx
│   ├── api.js
│   ├── components/
│   │   ├── FileUploader.jsx
│   │   └── TablePreview.jsx
│   └── main.jsx
├── tailwind.config.js
└── vite.config.js
