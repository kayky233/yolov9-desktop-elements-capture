import requests
from bs4 import BeautifulSoup
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt


def get_trade_data(item_id):
    url = f"https://www.youpin898.com/goodInfo?id={item_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to retrieve data")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    trades = soup.find_all('div', class_='record-item')

    data = []
    for trade in trades:
        price = float(trade.find('div', class_='price').text.strip().replace('￥', ''))
        trade_time = trade.find('div', class_='time').text.strip()
        data.append({
            "Price": price,
            "Trade Time": pd.to_datetime(trade_time)
        })

    df = pd.DataFrame(data)
    df.set_index("Trade Time", inplace=True)
    return df


# Get trade data
item_id = "109302"
df = get_trade_data(item_id)

# Check the data
print(df)

# Model the time series data
model = ARIMA(df['Price'], order=(5, 1, 0))
model_fit = model.fit(disp=0)

# Forecast the next day
forecast = model_fit.forecast(steps=1)[0]

# Plot the historical data and forecast
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Price'], label='Historical Prices')
plt.axvline(x=df.index[-1], color='red', linestyle='--', label='Forecast')
plt.plot([df.index[-1] + pd.Timedelta(days=1)], [forecast[0]], marker='o', markersize=5, color='red',
         label='Next Day Forecast')
plt.legend()
plt.title('Price Forecast for Next Day')
plt.xlabel('Date')
plt.ylabel('Price (￥)')
plt.show()

print(f"Predicted price for the next day: ￥{forecast[0]:.2f}")
