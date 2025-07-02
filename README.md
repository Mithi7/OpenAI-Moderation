# AI-Powered Content Moderation App

A Django-based application that performs **automated content moderation** using OpenAI’s `omni-moderation-latest` model. It detects harmful, unsafe, or inappropriate content across several categories and provides category-wise confidence scores.

---

## Key Features

- **Automated Content Screening**: Evaluates user-submitted text for potential violations.
- **Category Classification**:
  - Hate
  - Self-harm
  - Sexual content
  - Violence
  - With **subcategories** for deeper insight.
- **Category Confidence Scores**: Gives percentage-based scores indicating likelihood of violation.
- **Multilingual Support**: Designed for English, but accepts content in other languages too.
- **Powered by OpenAI**: Uses the `omni-moderation-latest` model via API.
- **Built with Django**: Clean structure with reusability and scalability in mind.

---

## Tech Stack

- **Backend**: Python, Django
- **AI**: OpenAI `omni-moderation-latest` model
- **Frontend**: HTML (template: `moderation.html`)
- **Database**: SQLite (default, can be changed)

---

## Project Structure

```
project_root/
├── app/
│   ├── migrations/
│   ├── static/js/
│   │   └── moderation.js
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── moderation/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   └── moderation.html
├── db.sqlite3
├── manage.py
├── requirements.txt
└── pyvenv.cfg
```

---

## How to Run the Project

### 1. Install Dependencies:

pip install -r requirements.txt

### 2. Set OpenAI API Key :

```setx OPENAI_API_KEY "your-openai-api-key" ``` (the key is set globally) or Set the key in local environment: ```$env:OPENAI_API_KEY = "openai-api-key"```

### 3. Run Django Server:

python manage.py runserver

### 4. Access App

Navigate to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

- Enter a sentence in the input box.
- Submit it for moderation.
- View results with confidence scores across categories.
- Review flags or violations if applicable.

---

## Notes

- Make sure your OpenAI key supports access to `omni-moderation-latest`.
- The app does not store user content or results.
- Extendable to support file uploads or batch analysis.
