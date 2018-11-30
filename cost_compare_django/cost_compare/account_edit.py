from os import listdir
from os.path import isfile, join
import json

files = [f for f in listdir('./pull_data') if isfile(join('./pull_data', f)) and not f.startswith('.')]

# print(files, '<--files')
# for i in range(len(files)):
# 	code = int(files[i].split('.')[0])
# 	print(code, type(code))

for i in range(len(files)):
	results = []
	with open('./pull_data/' + files[i], 'r') as f:
		data = json.load(f)
		federal_accounts = data["federal_accounts"]
		for j in range(len(federal_accounts)):
			results.append({
				"model": "cost_compare.Account_Key",
				"pk": 'a' + str(files[i].split('.')[0]) + 'fa' + str(federal_accounts[j]["federal_account_id"]),
				"fields": {
					"federal_account_id": federal_accounts[j]["federal_account_id"],
					"federal_account_name": federal_accounts[j]["federal_account_name"],
					"agency_id": int(files[i].split('.')[0])
				}
			})
	with open('seed_data/' + files[i].split('.')[0] + '.json', 'w') as outfile:
		json.dump(results, outfile)