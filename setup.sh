#!/bin/bash
echo "🚀 Setting up Dashboard API..."

# create virtual environment
python -m venv venv

# Activate
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# create .env from example
if [ ! -f .env ]; then
  cp .env.example .env
  echo "📄 Created .env from .env.example"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload"
```

**`.env.example`**
```
APP_NAME="Dashboard API"
MAX_FILE_SIZE_MB=10
ALLOWED_ORIGINS=["http://localhost:3000"]