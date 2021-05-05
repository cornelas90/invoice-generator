from flask import Flask, render_template, send_file, request
import os
from datetime import datetime
from weasyprint import HTML
import io
app = Flask(__name__)
#html = HTML('invoice.html')
#html.write_pdf('invoice.pdf')
@app.route('/', methods=['GET','POST'])
def hello_world():
	posted_json = request.get_json()
	posted_data = request.get_json() or {}
	today = datetime.today().strftime('%B %d, %Y')
	
	default_data = {
			'duedate': 'May 10, 2021',
			'from_addr': {
				'addr1': '198 8th Ave',
				'addr2': 'Cashville, TN 37202',
				'company_name': 'Bad Hombres Bean Barn'
			},
			'invoice_number': 656,
			'items': [{
			 'charge': 399.98,
			'title': 'Ethiopian Coffee Beans, Roasted in S. Korea'
		},
		{
			'charge': 749.99,
			'title': 'Biodegradable Cups (Bunny)'
		},
		{
			'charge': 799.99,
			'title': 'Kenji Lopez Autographed Mugs'
		}
	],
	'to_addr': {
		'company_name': 'Chuck\'s Cafe',
		'person_email': 'HansyPans@gmail.com',
		'person_name': 'Preston Hansen'
	}
	}

	duedate = posted_data.get('duedate', default_data['duedate'])
	from_addr = posted_data.get('from_addr', default_data['from_addr'])
	to_addr = posted_data.get('to_addr', default_data['to_addr'])
	invoice_number = posted_data.get('invoice_number', default_data['invoice_number'])
	items = posted_data.get('items', default_data['items'])

	#items = [{'title':'Website Design','charge': 300.00},
	#{'title':'Hosting (3 months)','charge': 75.00},
	#{'title':'Domain name (1 year)', 'charge': 10.00}]
	#duedate = 'August 1, 2018'
	total = sum([i['charge']for i in items])
	rendered = render_template('invoice.html', date = today, from_addr = from_addr, to_addr = to_addr, items = items, total = total, invoice_number = invoice_number, duedate = duedate)
	html = HTML(string=rendered)
	rendered_pdf = html.write_pdf()
	return send_file(io.BytesIO(rendered_pdf), attachment_filename='invoice.pdf')

if __name__ =='__main__':
	port = int(os.environ.get("PORT",5000))
	app.run(host='0.0.0.0', port=port)