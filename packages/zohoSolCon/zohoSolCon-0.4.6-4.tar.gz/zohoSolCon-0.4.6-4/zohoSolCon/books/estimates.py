import requests
import json


def format_header(token):
	return {
		"Authorization": f"Zoho-oauthtoken {token.access}"
	}
	
	
def create_estimate(token, org_id, data_object, line_items):
	url = f'https://books.zoho.com/api/v3/estimates?organization_id={org_id}'
	headers = format_header(token)
	
	data_object['line_items'] = line_items
	
	data = json.dumps(data_object).encode('utf-8')
	
	response = requests.post(url=url, headers=headers, data=data)
	
	if response.status_code == 400:
		token.generate()
                return create_estimate(token, org_id, data_object, line_items)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		try:
			estimate = content['estimate']
		except Exception as e:
			estimate = {"status":  response.status_code, "error": str(e)}
		return token, content.get("message"), estimate
		
		

def get_estimates(token, org_id, **kwargs):
	url = f'https://books.zoho.com/api/v3/estimates?organization_id={org_id}'
	headers = format_header(token)
	
	response = requests.get(url=url, headers=headers, params=kwargs)
	
	if response.status_code == 400:
		token.generate()
		return get_estimates(token, org_id, **kwargs)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		try:
			estimates = content['estimates']
			page_context = content['page_context']
		except Exception as e:
			estimates = [{"status": response.status_code, "error": str(e)}]
		
		return token, page_context, estimates
		
	
def update_estimate(token, org_id, estimate_id, data_object):
	url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}?organization_id={org_id}'
	headers = {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}
	
	data = json.dumps(data_object).encode("utf-8")
	
	response = requests.put(url=url, headers=headers, data=data)
	
	if response.status_code == 400:
		token.generate()
		return update_estimate(token, org_id, estimate_id, data_object)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		try:
			estimate = content['estimate']
		except Exception as e:
			estimate = {"status": response.status_code, "error": str(e)}
		
		return token, content.get("message"), estimate
		
		

def get_estimate(token, org_id, estimate_id, **kwargs):
	url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}?organization_id={org_id}'
	headers = {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}
	
	response = requests.get(url=url, headers=headers, params=kwargs)
	
	if response.status_code == 400:
		token.generate()
		return get_estimate(token, org_id, estimate_id, **kwargs)
	
	else:
		content = json.loads(response.content.decode('utf-8'))
		try:
			estimate = content['estimate']
		except Exception as e:
			estimate = {'status': response.status_code, 'error': str(e)}
			
		return token, estimate
		
		
def delete_estimate(token, org_id, estimate_id):
	url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}?organization_id={org_id}'
	headers = {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}
	
	response = requests.delete(url=url, headers=headers)
	
	if response.status_code == 400:
		token.generate()
		return delete_estimate(token, org_id, estimate_id)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		return token, content.get("message")
		

def mark_status(token, org_id, estimate_id, status):
	url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}/status/{status}?organization_id={org_id}'
	headers = {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}
	
	response = requests.post(url=url, headers=headers)
	
	if response.status_code == 400:
		token.generate()
		return mark_status(token, org_id, estimate_id, status)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		return token, content.get("message")
		

def estimate_approval(token, org_id, estimate_id, action):
	url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}/{action}?organization_id={org_id}'
	headers = {
		'Authorization': f'Zoho-oauthtoken {token.access}'
	}
	
	response = requests.post(url=url, headers=headers)
	
	if response.status_code == 400:
		token.generate()
		return submit_for_approval(token, org_id, estimate_id)
		
	else:
		content = json.loads(response.content.decode('utf-8'))
		return token, content.get("message")
		

def email_estimate(token, org_id, estimate_id, to_mail_ids, **kwargs):
        url = f'https://books.zoho.com/api/v3/estimates/{estimate_id}/email'
        headers = format_header(token)
        params = {'organization_id': org_id}

        data_object = kwargs
        data_object['to_mail_ids'] = to_mail_ids

        data = json.dumps(data_object).encode('utf-8')
        response = requests.post(url=url, headers=headers, params=params, data=data)
        if response.status_code == 401:
                token.generate()
                return email_estimate(token org_id, estimate_id, to_mail_ids, **kwargs)
        else:
                content = json.loads(response.content.decode('utf-8'))
                return token, content.get('message')
                
                
        

def mass_action(token, org_id, callback, **kwargs):
        next_page = True
        page = 1
        iterated = 0
        parameters = kwargs
        while next_page:
                url = f'https://books.zoho.com/api/v3/estimates?organization_id={org_id}'
                headers = {
                        'Authorization': f'Zoho-oauthtoken {token.access}'
                }
                parameters['page'] = str(page)
                parameters['per_page'] = '200'

                response = requests.get(url=url, headers=headers, params=parameters)
                if response.status_code == 400:
                        token.generate()
                        continue

                content = json.loads(response.content.decode('utf-8'))
                estimates = content['estimates']

                for record in estimates:
                        token, callback_response = callback(token, org_id, record)
                        print(callback_response)
                        iterated += 1
                        print(f'{iterated} Records Iterated')

                page_context = content['page_context']
                page += 1
                next_page = page_context['has_more_page']
        return token, f"{iterated} Records iterated \n===========\n Mass Operations complete."
        
                        
                
