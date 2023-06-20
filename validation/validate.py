from variables import env

def checkUrl():
    index = 0
    for char in env.PRICING_CALCULATOR_VALIDATOR:
        if char != env.PRICING_CALCULATOR_URL[index]:
            print("Error. the URL = ", env.PRICING_CALCULATOR_URL, " is not well written.\nMust start with:", env.PRICING_CALCULATOR_VALIDATOR)
            return False
        index += 1
    return True