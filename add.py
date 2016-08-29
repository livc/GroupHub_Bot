# encoding: utf-8
import json
import codecs
import base64
import sys

S1 = sys.argv[1]
for i in range(2, len(sys.argv)):
	S2 = sys.argv[i]
	with codecs.open('groups.json', 'r+', encoding='utf-8') as f:
		data = json.load(f)
		S2 = base64.b64encode(S2)
		data[S1.decode('utf-8')].append({'TEXT':S2})
		f.seek(0)
		json.dump(data, f, indent=4, ensure_ascii=False)

print 'success!'
