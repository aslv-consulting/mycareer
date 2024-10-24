# My career

A modern career manager.

## Development environment

1. Configure git

    ```bash
    git config commit.template ${PWD}/.git-templates/commit.txt
    ```

2. Virtual environment

    ```bash
    # Create it
    python3 -m venv .venv

    # Activate it
    source .venv/bin/activate

    # Upgrade the package installer
    pip install --upgrade pip

    # Install the required packages
    pip install -r .requirements/dev.txt -r .requirements/prod.txt
    ```

3. Run the app

    ```bash
    python3 -m mycareer
    ```

## Migration

```bash
# Create a migration
alembic revision --autogenerate -m"message"

# Migrate
alembic upgrade head

# Downgrade the last commit
alembic downgrade -1

# Downgrade until the commit
alembic downgrade <revision>

# Reset the database
alembic downgrade base
```

## Tests

```bash
pytest
```

## Changlog

The changelog is available [here](CHANGELOG.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
