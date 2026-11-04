class Lead:
    def __init__(self, prospect_name, product_name, last_contacted):
        self.prospect_name = prospect_name
        self.product_name = product_name
        self.last_contacted = last_contacted

    def next_action(self):
        if self.last_contacted <= 2:
            return 'Wait!'
        elif self.last_contacted <= 5:
            return 'Send a reminder'
        else:
            return 'Call now!'

    def __str__(self):
        return f'{self.prospect_name} is interested in buying {self.product_name}. Last contacted is {self.last_contacted} days ago, {self.next_action()}'

class LeadTracker:
    def __init__(self):
        self.leads = []

    def add_lead(self,prospect_name, product_name, last_contacted):
        if last_contacted < 0:
            return 'Last contacted cannot be a negative number'
        self.leads.append(Lead(prospect_name, product_name, last_contacted))
        return 'Lead successfully added'

    def find_lead(self, prospect_name):
        for lead in self.leads:
            if prospect_name.lower() == lead.prospect_name.lower():
                return lead
        return None

    def run_menu(self):
        while True:
            choice = input('1. View lead  2. Add lead  3. Quit:')
            if choice == '1':
                prospect_name = input('Enter the prospect name you want to view:')
                lead = self.find_lead(prospect_name)
                if lead is None:
                    print('Name not in list')
                else:
                    print(lead)
            elif choice == '2':
                prospect_name = input('Enter the prospect name you want to add to the lead:')
                product_name = input('Enter the product name:')
                try:
                    last_contacted = int(input('Enter the number of days last contacted: '))
                except ValueError:
                    print('Enter a number')
                    continue
                print(self.add_lead(prospect_name, product_name, last_contacted))
            elif choice == '3':
                break
            else:
                print('Invalid choice enter 1, 2, or 3')



tracker = LeadTracker()
tracker.add_lead('David', 'Shoes', 1)
tracker.add_lead('Sarah', 'Shirts', 4)
tracker.add_lead('Aisha', 'Bags', 5)
tracker.add_lead('Michael', 'Watches', 7)
tracker.run_menu()

            