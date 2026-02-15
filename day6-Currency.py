def usd_to_inr(usd):
    return usd * 83   # approx conversion from us to india

amount = float(input("Enter USD: "))
print("INR =", usd_to_inr(amount))
