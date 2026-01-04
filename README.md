# Superheroes API

A Flask REST API for managing superheroes and their powers.

## Features

- **Heroes Management**: Create, read, and manage superhero profiles
- **Powers Management**: Define and update superhero powers with descriptions
- **Hero-Powers Relationships**: Associate heroes with their powers and strength levels
- **Data Validation**: Ensures data integrity with built-in validations
- **RESTful Design**: Clean REST API endpoints following best practices

## Models

### Hero
- `id`: Primary key
- `name`: Hero's real name
- `super_name`: Hero's superhero name
- `hero_powers`: Relationship to powers through HeroPower

### Power
- `id`: Primary key
- `name`: Power name
- `description`: Power description (minimum 20 characters)
- `hero_powers`: Relationship to heroes through HeroPower

### HeroPower
- `id`: Primary key
- `strength`: Power strength level ('Strong', 'Weak', 'Average')
- `hero_id`: Foreign key to Hero
- `power_id`: Foreign key to Power
- `hero`: Relationship to Hero
- `power`: Relationship to Power

## API Endpoints

### Heroes
- `GET /heroes` - List all heroes (id, name, super_name only)
- `GET /heroes/<id>` - Get hero details with associated powers

### Powers
- `GET /powers` - List all powers
- `GET /powers/<id>` - Get power details
- `PATCH /powers/<id>` - Update power description

### Hero Powers
- `POST /hero_powers` - Create association between hero and power

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd superheroes-api
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   # Initialize migrations (if not already done)
   export FLASK_APP=run.py
   flask db init

   # Create migration
   flask db migrate -m "create tables"

   # Apply migrations
   flask db upgrade
   ```

5. **Seed the database**
   ```bash
   python seed.py
   ```

6. **Run the application**
   ```bash
   python run.py
   ```

The API will be available at `http://127.0.0.1:5000`

## Usage Examples

### Get all heroes
```bash
curl http://127.0.0.1:5000/heroes
```

### Get hero details
```bash
curl http://127.0.0.1:5000/heroes/1
```

### Get all powers
```bash
curl http://127.0.0.1:5000/powers
```

### Update power description
```bash
curl -X PATCH http://127.0.0.1:5000/powers/1 \
  -H "Content-Type: application/json" \
  -d '{"description": "Updated description with at least 20 characters"}'
```

### Create hero-power association
```bash
curl -X POST http://127.0.0.1:5000/hero_powers \
  -H "Content-Type: application/json" \
  -d '{"strength": "Strong", "power_id": 1, "hero_id": 1}'
```

## Project Structure

```
superheroes-api/
│
├─ app/
│  ├─ __init__.py    # Application factory
│  ├─ models.py      # Database models
│  ├─ routes.py      # API routes (blueprints)
│  └─ config.py      # Configuration
│
├─ instance/         # SQLite database
├─ migrations/       # Flask-Migrate files
├─ run.py           # Application entry point
├─ seed.py          # Database seeding script
├─ requirements.txt # Python dependencies
└─ README.md        # This file
```

## Technologies Used

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Migrate**: Database migrations
- **SQLAlchemy-Serializer**: Model serialization
- **SQLite**: Database (development)

## Validation Rules

- **HeroPower.strength**: Must be 'Strong', 'Weak', or 'Average'
- **Power.description**: Must be present and at least 20 characters long

## Error Handling

The API returns appropriate HTTP status codes and JSON error messages:

- `404 Not Found`: Resource not found
- `400 Bad Request`: Validation errors or malformed requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
