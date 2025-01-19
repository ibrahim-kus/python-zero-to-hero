
import requests
import json

api_key = "xxxxxxxxxxxxxxxxxxxxxx"
#GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

currency = input("to be converted currency: ") #USD
exchanged_currency = input("to be returned currency: ") #TRY
amount = int(input(f"How much {currency} do you want to exchange? : "))

result = requests.get(api_url + currency)
result_json = json.loads(result.text)

#print(result_json)
#print(result_json["conversion_rates"][exchanged_currency])
print("1 {0} = {1} {2}".format(currency,result_json["conversion_rates"][exchanged_currency], exchanged_currency))
print("{0} {1} = {2} {3}".format(amount,currency, amount * result_json["conversion_rates"][exchanged_currency], exchanged_currency))