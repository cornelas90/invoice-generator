import requests

url = 'http://127.0.0.1:5000/'
data = {
	'duedate': 'May 10, 2021',
	'from_addr': {
		'addr1': '138 8th Ave',
		'addr2': 'Cashville, TN 37212',
		'company_name': 'Bad Hombres Bean Barn'
	},
	'invoice_number': 9000,
	'items': [{
		'charge': 200.00,
		'title': 'Portillos'
		},
		{
		'charge': 8.99,
		'title': 'Gardiniera'
		},
		{
		'charge': 19.99,
		'title': 'Old Style'
		}
	],
	'to_addr': {
		'company_name': 'Chicago Wish List',
		'person_email': 'CornyBoy@gmail.com',
		'person_name': 'Christian Ornelas'
	}
}

html = requests.post(url, json=data)

with open('invoice.pdf', 'wb') as f:
	f.write(html.content)