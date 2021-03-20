theAccountOfTheEmir = {
    'name': 'Emirhan ŞİRİNOĞLU',
    'accountnumber': '12356480',
    'balance': 2000,
    'additionalaccount': 2000
}

theAccountOfTheAhmet = {
    'name': 'Ahmet ŞİRİNOĞLU',
    'accountnumber': '22153471',
    'balance': 3000,
    'additionalaccount': 1000
}

def withdrawMoney(account, quantity):
    print(f"Hello {account['name']} Welcome.")

    if (account['balance'] >= quantity):
        account['balance'] -= quantity
        print("you can get your money.")
        moneyInquiry(account)
    else:
        total = (account['balance'] + account['additionalaccount'])
        
        if (total >= quantity):
            additionalAccountUsage = input('Your balance is not sufficient for withdrawal. Would you like to continue using your additional account ? (y/n)') 
            if additionalAccountUsage == 'y':
                amountToBeUsedForAdditionalAccount = quantity - account['balance']
                account['balance'] = 0
                account['additionalaccount'] -= amountToBeUsedForAdditionalAccount
                print('you can get your money.')
                moneyInquiry(account)
            else:
                print(f"{account['accountnumber']} on your account {account['balance']} TL available.")
        else:
            print('Insufficient balance, your transaction failed.')
            moneyInquiry(account)

def moneyInquiry(account):
    print(f"{account['accountnumber']} at your numbered account {account['balance']} TL available. Your additional account as well {account['additionalaccount']} TL  available.")
       
withdrawMoney(theAccountOfTheEmir,2000)
print('***************')     
withdrawMoney(theAccountOfTheEmir,2000)
