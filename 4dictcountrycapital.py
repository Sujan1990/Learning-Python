country_capital = {
    "Germany" : "Berlin",
    "South Korea" : "Seoul",
    "Nepal" : "Kathmandu",
    "England" : "London",
    "China" : "Beijing",
}

# print(f"Capital city of Germany is {country_capital['Germany']}")
# print(f"Capital city of South Korea is {country_capital['South Korea']}")
# print(f"Capital city of Nepal is {country_capital['Nepal']}")

#below country is key and capital is value so while using loop we use the variable "k"

for country in country_capital:
    print(f"The capital city of {country} is {country_capital[country]}")