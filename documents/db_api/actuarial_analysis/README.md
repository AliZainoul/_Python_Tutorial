# Actuarial Analysis Application

An SQLAlchemy-based application for actuarial analysis with realistic simulated insurance data.

## 🏗️ Architecture

This project follows clean architecture principles with clear separation of concerns:

### Design Principles Applied

- **DRY (Don't Repeat Yourself)**: Reusable components and utility functions
- **Separation of Concerns**: Clear boundaries between data, business logic, and presentation
- **Single Responsibility**: Each module has one well-defined purpose
- **Dependency Injection**: Configuration and dependencies passed explicitly
- **Type Hints**: Full type annotations for better IDE support and maintainability

### Project Structure

```md
actuarial_analysis/
│
├── config/                      # Configuration layer
│   ├── __init__.py
│   └── settings.py              # All configuration constants
│
├── src/
│   ├── models/                  # Data models (ORM)
│   │   ├── base.py              # Base declarative configuration
│   │   ├── client.py            # Client model
│   │   ├── contract.py          # Contract model
│   │   ├── prime.py             # Premium payment model
│   │   └── claim.py             # Claim model
│   │
│   ├── database/                # Database infrastructure
│   │   ├── connection.py        # Engine and session management
│   │   └── setup.py             # Schema setup utilities
│   │
│   ├── services/                # Business logic
│   │   ├── data_generator.py   # Data generation service
│   │   └── analytics.py         # Analytics calculations
│   │
│   └── utils/                   # Shared utilities
│       └── date_helpers.py      # Date manipulation functions
│
├── main.py                      # Application entry point
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd actuarial_analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Application

```bash
python main.py
```

## 📊 Features

The application generates realistic insurance data and computes:

1. **Average Premium by Age Bucket**: Analyzes premiums across different age groups (0-25, 26-45, 46-65, 66+)
2. **Claim Frequency**: Calculates claim rates per product and year
3. **Average Claim Cost by Segment**: Compares individual vs corporate segments
4. **Claim-to-Premium Ratio**: Measures profitability by product

## 🔧 Configuration

All configuration is centralized in `config/settings.py`:

- **Database**: Connection URL, echo settings
- **Data Generation**: Number of clients, probabilities, date ranges
- **Analysis**: Reference dates, year ranges for analysis

Example customization:

```python
# config/settings.py
@dataclass
class DataGenerationConfig:
    n_clients: int = 500  # Increase from 200
    corporate_probability: float = 0.2  # Increase corporate clients
```

## 🏛️ Key Components

### Models Layer

ORM models representing database entities:

- `Client`: Insurance customers (individual/corporate)
- `Contract`: Insurance policies
- `Prime`: Premium payments
- `Claim`: Insurance claims

### Database Layer

- `DatabaseManager`: Handles engine and session lifecycle
- `DatabaseSetup`: Schema creation/migration utilities

### Services Layer

- `DataGenerator`: Creates realistic simulated data
- `AnalyticsService`: Computes actuarial indicators

### Utils Layer

- `date_helpers`: Age calculation, date manipulation, bucket classification

## 🎯 Design Benefits

- ✅ 10+ focused modules (50-150 lines each)
- ✅ Clear module boundaries
- ✅ Easy to unit test
- ✅ Simple to add new features
- ✅ Centralized configuration
- ✅ Reusable components

## 🧪 Testing

The modular structure makes testing straightforward:

```python
# Example test structure
def test_age_calculation():
    birth = date(2000, 1, 1)
    ref = date(2025, 1, 1)
    assert calculate_age(birth, ref) == 25

def test_data_generator():
    config = DataGenerationConfig(n_clients=10)
    generator = DataGenerator(config)
    # Test generation logic
```

## 📈 Extending the Application

### Adding a New Model

1. Create file in `src/models/`
2. Define ORM model extending `Base`
3. Add relationships to existing models

### Adding New Analytics

1. Add method to `AnalyticsService`
2. Create presentation function in `main.py`
3. Call from main routine

### Changing Configuration

Simply update values in `config/settings.py` - all services will use new values.

## 🤝 Contributing

When contributing, maintain:

- Type hints on all functions
- Docstrings (Google style)
- Single responsibility per function/class
- Configuration externalized to `config/`

## 📝 License

MIT License

## 👥 Authors

<claude.ai>
<ali.zainoul.az@gmail.com>
