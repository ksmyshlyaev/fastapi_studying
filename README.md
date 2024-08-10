# fastapi_studying

### Launching the backend project

`uvicorn app.main:app --reload`

### Add a new migration

**DON'T FORGET TO IMPORT NEW MODELS IN ALEMBIC ENV.PY!!!**

`alembic revision --autogenerate -m "Migration test message"`

### Run all migrations

`alembic upgrade head`
