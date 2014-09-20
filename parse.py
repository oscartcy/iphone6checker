import json, sys

obj=json.load(sys.stdin)
for model, m in obj.iteritems(): 
	if (isinstance(m, dict)):
		for s, a in m.iteritems(): 
			if (a == True): 
				print '1'
