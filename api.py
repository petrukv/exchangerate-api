import requests


def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        rate = data['rates'].get(target_currency)
        
        if rate is not None:
            return rate
        else:
            return f"Курс для {target_currency} не знайдено."
    else:
        return f"Не вдалося отримати курс. Код помилки: {response.status_code}"

base_currency = "USD"
target_currency = "UAH"
exchange_rate = get_exchange_rate(base_currency, target_currency)
print("---------------------------------------------")
print(f"Курс {base_currency} до {target_currency}: {exchange_rate}")
