w=float(input("Enter your daily wages: "))
d=int(input("Enter number of days: "))
daily_wages=w*d
HRA=daily_wages*0.1 #House rent allowence
TA=daily_wages*0.05 #Travel Allowence
PT=daily_wages*0.02 #Professional Tax
gross_amt=HRA+TA+daily_wages
net_amt=gross_amt-PT
print("---------//------------------//-----------------//-----------")
print("The gross salary (before tax deduction) is:",gross_amt)
print("The total salary payable is:",net_amt)

