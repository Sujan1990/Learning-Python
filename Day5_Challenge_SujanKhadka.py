#Create a program that coverts Nepali Currency to USD, EUTO and Japanese Yen

print("CURRENCY CONVERTER AS ON 24.06.2024")

nrs=int(input("Enter amount in NRS: "))

usd=nrs*0.0075
euro=nrs*0.007
yen=nrs*1.19

print(f"NRS: {nrs} in USD is {usd}")
print(f"NRS: {nrs} in EUR is {euro}")
print(f"NRS: {nrs} in JPY is {yen}")
