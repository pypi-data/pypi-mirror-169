-> REQUIREMENTS

command: pip install -r requirements.txt

-> MIGRATIONS

To generate a new migration script
command: alembic revision --autogenerate -m <"name">

To upgrade to most recent version
command: alembic upgrade head

To downgrade to previous version
command: alembic downgrade -1

-> TESTS

Note: first move into tests directory

To run all tests
command: pytest

To run specific tests
command: pytest <path to file>

->FASTAPI

command: uvicorn app.app:app --reload

or

command: python main.py