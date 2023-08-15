import json
phonebook = 'pb.json'

def save_phonebook(phone_data):
    with open(phone_data, 'w', encoding='utf-8') as f:
 	    f.write(json.dumps(phone_data, indent=3, ensure_ascii=False))