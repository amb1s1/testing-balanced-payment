import balanced

balanced.configure(<api_key>) #replace api_key with yours

#Creating New Customer

new_customer = balanced.Customer(
          name = 'Eveline Lee',
          email = 'elee@gmail.com',
          ssn_last4 ='6058',
          business_name = 'Associate',
          address = {'line1' : '9 Shaefer St', 'city': 'brooklyn', 'postla_code':'11207'},
          phone = '2019560100',
          dod = '1978-02',
          facebook = 'evilee',
          twitter = 'evilee',

          )

#Save new_customer without this is not going to be on balanced vault
new_customer.save()

#Adding a card to the new customer
#I need to create a card  token for testing - Later I need to use the balanced.js for pci comply
card_token = balanced.Marketplace().create_card(
     name='Eveline Lee',
     card_number='341111111111111',
     expiration_year='2015',
     expiration_month='09',
     postal_code = '11207',
     security_code = '123',
     )
#I need to find the customer that I want to add this card
#The  URI that I'm passing, I can save that on my database
customer = balanced.Customer.find(new_customer.uri) 
#Now I will be adding the card to the user
customer.add_card(card_token.uri)

#How to charge to Customer
#Find Customer
customer = balanced.Customer.find(<customer.uri>)
#Charging the card
customer.debit(
    appears_on_statement_as='Statement text',
    amount='5000',
    description='Some descriptive text for the debit in the dashboard',
)

