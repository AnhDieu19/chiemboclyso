# Security Setup Guide

## 🔴 CRITICAL: First-Time Setup

Before running the application, you MUST configure the following security settings:

### 1. Environment Variables Setup

**Step 1: Copy the example file**
```bash
cp .env.example .env
```

**Step 2: Generate a secure SECRET_KEY**
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output and paste it in `.env` as the `SECRET_KEY` value.

**Step 3: Add your Gemini API Key**

Get your API key from: https://makersuite.google.com/app/apikey

Add it to `.env` as the `GEMINI_API_KEY` value.

**Example .env file:**
```bash
SECRET_KEY=your_generated_secret_key_here_64_characters_long
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=sqlite:///tuvi.db
FLASK_ENV=development
FLASK_DEBUG=True
```

### 2. Verify .env is Ignored by Git

Make sure `.env` is listed in `.gitignore`:

```bash
# Check if .env is in .gitignore
grep -n "^\.env$" .gitignore
```

If not found, add it:
```bash
echo ".env" >> .gitignore
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Load Environment Variables

The application will automatically load `.env` using `python-dotenv`.

**For manual testing:**
```bash
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print('SECRET_KEY:', 'Set' if os.getenv('SECRET_KEY') else 'Not Set')"
```

## 🔒 Security Checklist

- [ ] Created `.env` file with secure SECRET_KEY
- [ ] Added valid GEMINI_API_KEY to `.env`
- [ ] Verified `.env` is in `.gitignore`
- [ ] Never committed `.env` to version control
- [ ] Rotated any previously exposed API keys
- [ ] Used different SECRET_KEY for production vs development

## 🚀 Running the Application

**Development mode:**
```bash
cd backend
python app.py
```

The application will run on http://localhost:5001

**Production mode:**
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
gunicorn -w 4 -b 0.0.0.0:8000 backend.app:create_app()
```

## ⚠️ Important Security Notes

1. **NEVER** commit `.env` file to version control
2. **NEVER** hardcode secrets in source code
3. **ALWAYS** use different keys for development and production
4. **ROTATE** API keys immediately if they are exposed
5. **LIMIT** API key permissions to minimum required access

## 🔄 If API Key Was Previously Exposed

If the Gemini API key was committed to the repository:

1. **Immediately rotate the key** in Google Cloud Console
2. **Revoke the old key** to prevent unauthorized usage
3. **Check billing** for any unauthorized API calls
4. **Update `.env`** with the new key
5. **Review git history** to ensure no other secrets were exposed

## 📚 Additional Resources

- [Flask Security Best Practices](https://flask.palletsprojects.com/en/2.3.x/security/)
- [Google Cloud API Key Best Practices](https://cloud.google.com/docs/authentication/api-keys)
- [OWASP Security Guidelines](https://owasp.org/www-project-top-ten/)
