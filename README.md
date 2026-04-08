# Smart Expense Tracker — AI Microservice

FastAPI + Groq LLaMA 3.3 chat endpoint for personalized financial advice.

## Setup
```bash
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn groq python-dotenv
```

Add `.env`:
```
GROQ_API_KEY=your_key
```
```bash
uvicorn main:app --reload --port 8000
```

## Related
- [Backend](https://github.com/voidirl/ai-expense-tracker-backend)
- [Frontend](https://github.com/voidirl/ai-expense-tracker-frontend)
## 🌐 Live Demo
[![Live Demo](https://img.shields.io/badge/Live%20Demo-voidledger.vercel.app-black?style=for-the-badge&logo=vercel)](https://voidledger.vercel.app)
