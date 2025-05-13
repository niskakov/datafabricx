def normalize_column_names(columns: list[str]) -> list[str]:
    # Простая семантическая нормализация
    mapping = {
        'date of payment': 'дата',
        'payment_date': 'дата',
        'name': 'имя',
        'full name': 'имя',
        'amount': 'сумма',
        'price': 'сумма',
    }
    return [mapping.get(col.strip().lower(), col.strip().lower()) for col in columns]
