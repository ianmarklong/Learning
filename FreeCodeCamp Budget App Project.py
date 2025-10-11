class Category():
    def __init__(self,cat):
        self.ledger = []
        self.cat = cat
    
    def __str__(self):
        result = ''
        start = (30-len(self.cat))//2
        header = '*'*start + self.cat + '*'*(30-len(self.cat)-start) + '\n'
        result += header

        for each in self.ledger:
            desc = '{:<23}'.format(each['description'][:23])
            amount = '{:>7.2f}'.format(each['amount'])
            result += desc+amount+'\n'

        result += 'Total: ' +str(self.get_balance())

        return result
    
    
    def deposit(self,amount,description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self,amount,description = ''):
        #check if sufficient funds
        if self.check_funds(amount):
            amount = amount * (-1)
            self.ledger.append({'amount': amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for each in self.ledger:
            total += each['amount']
        return total
    
    def transfer(self,amount,category):
        #category is an object

        if not self.check_funds(amount):
            return False

        desc1 = f'Transfer to {category.cat}'
        self.withdraw(amount,desc1)

        desc2 = f'Transfer from {self.cat}'
        category.deposit(amount,desc2)
        return True

    def check_funds(self,amount):
        balance = self.get_balance()
        if amount > balance:
            return False
        return True

def create_spend_chart(categories):
    result = 'Percentage spent by category\n'
    spendages = []
    percentages = []
    total = 0
    for cat in categories:
        spent = 0
        for each in cat.ledger:
            if each['amount'] < 0:
                spent += each['amount']

        spent = spent * (-1)
        total+=spent
        spendages.append(spent)
    for spendage in spendages:
        percentage = int((spendage / total) * 100)
        percentage = percentage // 10 * 10
        percentages.append(percentage)

        
    for i in range(100, -1, -10):
        line = '{:>3}| '.format(i)
        for p in percentages:
            if p >= i:
                line += 'o  '
            else:
                line += '   '
        result += line + '\n'


    number = 1 + len(categories)*3
    result += '    '+'-'*number + '\n'

    #find longest cat name
    longest = 0
    names = [] 
    for j in categories:
        names.append(j.cat)
        if len(j.cat)>longest:
            longest = len(j.cat)
    
    for k in range(longest):
        nameLine = '     '
        for name in names:
            try:
                nameLine += name[k] + '  '
            except:
                nameLine += '   '
        if k == longest-1:
            result += nameLine
        else:
            result += nameLine + '\n'



    return result

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(310.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

clothing.deposit(1000, 'deposit')
clothing.withdraw(510.15, 'groceries')
clothing.withdraw(15.89, 'restaurant and more food for dessert')

auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(310.15, 'groceries')
auto.withdraw(15.89, 'restaurant and more food for dessert')

list = [food,clothing,auto]
print(create_spend_chart(list))
