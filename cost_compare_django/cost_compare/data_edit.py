import json

# agency spending
# agency_results = []
# with open('data/agency_spending.json', 'r') as f:
# 	data = json.load(f)
# 	data_results = data["results"]
# 	print(len(data_results), '<--length')
# 	for i in range(len(data_results)):
# 		agency_results.append({
# 			"model": "cost_compare.Agency_Raw",
# 			"pk": i,
# 			"fields": {
# 				"name": data_results[i]["name"],
# 				"agency_id": data_results[i]["id"],
# 				"amount": data_results[i]["amount"],
# 				"code": data_results[i]["code"],
# 				"category": data_results[i]["type"]
# 			}
# 			})
# 	print(agency_results, '<--results')

# with open('data/agency_spending_raw_dump.json', 'w') as outfile:
# 	json.dump(agency_results, outfile)

# federal account spending
account_results = []
with open('data/federal_account_spending.json', 'r') as f:
	data = json.load(f)
	data_results = data["results"]
	print(len(data_results), '<--length')
	for i in range(len(data_results)):
		account_results.append({
			"model": "cost_compare.Federal_Account_Raw",
			"pk": i,
			"fields": {
				"name": data_results[i]["name"],
				"account_id": data_results[i]["id"],
				"account_number": data_results[i]["account_number"],
				"code": data_results[i]["code"],
				"amount": data_results[i]["amount"],
				"category": data_results[i]["type"]
			}
			})

with open('data/federal_account_spending_raw_dump.json', 'w') as outfile:
	json.dump(account_results, outfile)

# toptier agency spending--no longer in use
# results = []
# with open('./toptier_agency_spending.json', 'r') as f:
# 	# print(f, '<--f')
# 	data = json.load(f)
# 	data_results = data["results"]
# 	data_results_0 = data_results[0]
# 	for i in range(5):
# 		# print(data_results[i], '--',i,'--')
# 		results.append({
# 			"model": "cost_compare.Agency_Raw",
# 			"pk": i+1,
# 			"fields": {
# 				"percentage_of_total_budget_authority": data_results[i]["percentage_of_total_budget_authority"],
# 				"budget_authority_amount": data_results[i]["budget_authority_amount"],
# 				"obligated_amount": data_results[i]["obligated_amount"],
# 				"active_fq": data_results[i]["active_fq"],
# 				"active_fy": data_results[i]["active_fy"],
# 				"outlay_amount": data_results[i]["outlay_amount"],
# 				"abbreviation": data_results[i]["abbreviation"],
# 				"agency_id": data_results[i]["agency_id"],
# 				"agency_name": data_results[i]["agency_name"],
# 				"current_total_budget_authority_amount": data_results[i]["current_total_budget_authority_amount"]
# 			}
# 			})
# 	print(results, '<--results')

# with open('toptier_agency_raw_dump.txt', 'w') as outfile:
# 	json.dump(results, outfile)

# with open('toptier_agency_raw_dump.json', 'w') as outfile:
# 	json.dump(results, outfile)

