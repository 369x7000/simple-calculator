# SimpleCalculator and CurrencyConverter

## Overview

This repository contains two Python projects:

1. **SimpleCalculator**: A basic calculator app built using the Kivy framework.
2. **CurrencyConverter**: A currency exchange application using the Tkinter framework and Fixer.io API for real-time exchange rates.

## Requirements

### General Requirements

- Python 3.6 or higher
- Internet connection for the CurrencyConverter (to fetch exchange rates)

### SimpleCalculator Requirements

- Kivy

### CurrencyConverter Requirements

- Requests
- Tkinter

## Installation

### Clone the Repository

```sh
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

### Install Dependencies

#### SimpleCalculator

```sh
pip install kivy
```

#### CurrencyConverter

```sh
pip install requests
```

## Usage

### SimpleCalculator

1. Navigate to the `SimpleCalculator` directory.
2. Run the `calculator.py` file.

```sh
python calculator.py
```

The calculator GUI will launch, allowing you to perform basic arithmetic operations.

### CurrencyConverter

1. Navigate to the `CurrencyConverter` directory.
2. Run the `currency_exchanger.py` file.

```sh
python currency_exchanger.py
```

The currency converter GUI will launch. You can enter the amount, select the currencies, and perform the conversion.

## Code Overview

### SimpleCalculator

- **calculator.py**: Contains the implementation of a basic calculator using Kivy.
  - `SimpleCalculator(App)`: Main application class that builds the UI.
  - `on_button_press(self, instance)`: Handles button press events.
  - `on_solution(self, instance)`: Evaluates the expression and displays the result.

### CurrencyConverter

- **currency_exchanger.py**: Contains the implementation of a currency converter using Tkinter.
  - `get_exchange_rates()`: Fetches the latest exchange rates from Fixer.io API.
  - `convert_currency(amount, from_currency, to_currency, rates)`: Converts the amount from one currency to another.
  - `perform_conversion()`: Retrieves user input, performs conversion, and updates the GUI with the result.

## Configuration

### CurrencyConverter API Key

The CurrencyConverter uses Fixer.io API to get exchange rates. Replace the `API_KEY` in `currency_exchanger.py` with your own API key from Fixer.io.

```python
API_KEY = "your_api_key_here"
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any inquiries or issues, please contact [your-email@example.com](mailto:your-email@example.com).

---

Thank you for using SimpleCalculator and CurrencyConverter!
