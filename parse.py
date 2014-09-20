import json, sys

stores = {'R409': 'Hyson', 'R428': 'ifc', 'R485': 'FW'}
models = {
	u'MGA82ZP/A': 'iPhone 6 Plus  16G Grey  ', 
	u'MGA92ZP/A': 'iPhone 6 Plus  16G Silver', 
	u'MGAA2ZP/A': 'iPhone 6 Plus  16G Gold  ', 
	u'MGAH2ZP/A': 'iPhone 6 Plus  64G Grey  ', 
	u'MGAJ2ZP/A': 'iPhone 6 Plus  64G Silver', 
	u'MGAK2ZP/A': 'iPhone 6 Plus  64G Gold  ', 
	u'MGAC2ZP/A': 'iPhone 6 Plus 128G Grey  ', 
	u'MGAE2ZP/A': 'iPhone 6 Plus 128G Silver', 
	u'MGAF2ZP/A': 'iPhone 6 Plus 128G Gold  ', 
	u'MG472ZP/A': 'iPhone 6       16G Grey  ', 
	u'MG482ZP/A': 'iPhone 6       16G Silver', 
	u'MG492ZP/A': 'iPhone 6       16G Gold  ', 
	u'MG4F2ZP/A': 'iPhone 6       64G Grey  ', 
	u'MG4H2ZP/A': 'iPhone 6       64G Silver', 
	u'MG4J2ZP/A': 'iPhone 6       64G Gold  ', 
	u'MG4A2ZP/A': 'iPhone 6      128G Grey  ', 
	u'MG4C2ZP/A': 'iPhone 6      128G Silver', 
	u'MG4E2ZP/A': 'iPhone 6      128G Gold  '};


obj=json.load(sys.stdin)
ret=False
for store in stores.keys(): 
	for model in models.keys(): 
		if (obj[store][model] == True): 
			ret=True
			sys.stderr.write(stores[store] + ' ' + models[model] + '\n')
if (ret == True): 
	print '1'
