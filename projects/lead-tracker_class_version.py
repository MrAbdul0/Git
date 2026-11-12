

class Lead:
    def __init__(self, prospect, product, last_contacted):
        self.prospect = prospect
        self.product = product
        self.last_contacted = last_contacted

    def next_action(self):
        if self.last_contacted <= 2:
            return 'Wait!'
        elif self.last_contacted <= 5:
            return 'Send a reminder'
        else:
            return 'Call now!'

    def __str__(self):
        return f'{self.prospect} is interested in buying {self.product}. Last contacted is {self.last_contacted} days ago, {self.next_action()}'

class LeadTracker:
    def __init__(self):
        self.leads = []

    def add_lead(self,prospect, product, last_contacted):
        prospect = prospect.strip().lower()
        product = product.strip().lower()

        for lead in self.leads:
            if prospect == lead.prospect and product == lead.product:
                raise ValueError('Lead with this prospect and product already exists')

        if not prospect or not product:
            raise ValueError('Prospect or product cannot be empty')
        
        
        if last_contacted < 0:
            raise ValueError('Last contacted cannot be a negative number')

        if not isinstance(last_contacted, int):
            raise ValueError('Last contacted must be an integer')
        self.leads.append(Lead(prospect, product, last_contacted))
        return 'Lead successfully added'

    def find_lead(self, prospect):
        prospect = prospect.strip().lower()

        if not prospect:
            raise ValueError('Prospect name cannot be empty')
        
        for lead in self.leads:
            if prospect not in lead.prospect:
                continue
            return lead
        raise ValueError('Prospect not found')

    def run_menu(self):
        while True:
            choice = input('1. View lead  2. Add lead  3. Quit:')
            if choice == '1':

                try:
                    prospect = input('Enter the prospect name you want to view:')
                    lead = self.find_lead(prospect)
                    print(lead)
                except ValueError as e:
                    print(e)

            elif choice == '2':
                try:
                    prospect = input('Enter the prospect name you want to add to the lead:')
                    product = input('Enter the product name:')
                    try:
                        last_contacted = int(input('Enter the number of days last contacted: '))
                    except ValueError:
                        print('Last contacted must be an integer')
                        continue
                    print(self.add_lead(prospect, product, last_contacted))
                except ValueError as e:
                    print(e)
                                   
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

            