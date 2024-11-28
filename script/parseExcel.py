from argparse import ArgumentParser
import pandas as pd

prodInfo = {}

def read_product(productCsv):
	product = pd.read_csv(productCsv)
	for index, row in product.iterrows():
		prodInfo[row[0]] = {'id':row[1], 'unit':row[2]}

def summarize(noList):
	summarizeData = {}
	for v1 in noList:
		print(noList[v1]['time'])
		for v2 in noList[v1]['item']:
			if v2['Name'] in prodInfo:
				print(v2['Name'], prodInfo[v2['Name']]['id'])
				if prodInfo[v2['Name']]['id'] in summarizeData:
					if v2['Name'] in summarizeData[prodInfo[v2['Name']]['id']]:
						summarizeData[prodInfo[v2['Name']]['id']][v2['Name']].append({
							'id':v1,
							'time':noList[v1]['time'],
                            'total':v2['Total']
						})
					else:
						summarizeData[prodInfo[v2['Name']]['id']][v2['Name']] = [{
							'id':v1,
							'time':noList[v1]['time'],
                            'total':v2['Total']
						}]
				else:
					info = [{
						'id':v1,
						'time':noList[v1]['time'],
						'total':v2['Total']
					}]
					print(prodInfo[v2['Name']]['id'])
					#summarizeData[prodInfo[v2['Name']]['id']][v2['Name']] = info
def dumpData(noList):
	output_string = "Flag,發票號碼,日期,開立時間,載具,統編,名稱,數量,單價,金額\n"
	for v1 in noList:
		output_string += f"0,{v1},{noList[v1]['date']},{noList[v1]['time']},{noList[v1]['Carrier']},{noList[v1]['CustomerID']},{noList[v1]['Type']},{noList[v1]['Price']},{noList[v1]['Tax']},{noList[v1]['Total']}\n".replace('nan','')
		i = 1
		for v2 in noList[v1]['item']:
			output_string += f"{i},{v1},{noList[v1]['date']},{noList[v1]['time']},{noList[v1]['Carrier']},{noList[v1]['CustomerID']},{v2['Name']},{v2['Num']},{v2['UnitPrice']},{v2['Total']}\n".replace('nan','')
			i += 1
	print(output_string)

def parseExcel(excel_file):
	s1 = pd.read_excel(excel_file, sheet_name=0)
	s2 = pd.read_excel(excel_file, sheet_name=1)
	invalid_no = []
	noList = {}
	for index, row in s1.iterrows():
		if row[0] == 3:     #作廢
			invalid_no.append(row[2])
		else:
			noList[row[2]] = {
				'date': row[3],
				'time': row[4],
				'Carrier': row[8],
				'CustomerID': row[11],
				'Price': row[14],
				'Tax': row[19],
				'Total': row[7],
				'Type': 2 if (row[14]==row[7]) else 3,
			}
	for index, row in s2.iterrows():
		if row[0] in invalid_no:
			None
		else:
			if noList[row[0]].get('item') == None:
				noList[row[0]]['item'] = [{'Name':row[2], 'Num': row[3], 'UnitPrice': row[5], 'Total': row[6]}]
			else:
				noList[row[0]]['item'].append({'Name':row[2], 'Num': row[3], 'UnitPrice': row[5], 'Total': row[6]})
	dumpData(noList)
	#summarize(noList)

read_product("product.csv")

parser = ArgumentParser()
parser.add_argument("-i", "--input-file", dest="input_file")
args = parser.parse_args()
if(len(args.input_file) > 0):
    parseExcel(args.input_file)

