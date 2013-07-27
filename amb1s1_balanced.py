import balanced

balanced.configure("api_key") #replace api_key with yours

Getting the user uri = Key
card = balanced.Marketplace().my_marketplace.create_buyer(name='Anna Karina Lee',
                    card_number='5105105105105100',
                    expiration_month='11',
                    expiration_year='2015',
                    security_code='123',
                    street_address='34-13 Southern Drive',
                    city='Fair Lawn',
                    region=None,
                    postal_code='07410',
                    country_code=None,
                    phone_number='20195601',
                    )