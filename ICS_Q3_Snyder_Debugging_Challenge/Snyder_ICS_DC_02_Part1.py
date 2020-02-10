#Alem Snyder
#print items in a deceonary
Items = {"Milk":6.50,
         "Bread": 4.99,
         "Butter": 7.35,
         "Bananas":.19,
         "Oatmeal (1lb)":2.00,
         "Chicken":12.35,}

for name,price in Items.items():
    print(f'{" "*(10-(len(name)+len(str(price)))/2)}{name}      {str(price)}')

#Should print

#       Milk     6.5
#      Bread     4.99
#     Butter     7.35
#     Bananas     0.19
#  Oatmeal (1lb)     2.0
#    Chicken     12.35
