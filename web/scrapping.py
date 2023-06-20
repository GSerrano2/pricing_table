import requests
from variables import env

def getWeb():
    try:
        response = requests.get(env.PRICING_CALCULATOR_URL)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None