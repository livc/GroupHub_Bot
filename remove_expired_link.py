import json
import base64
import requests
import time
import codecs

with open ('groups.json', 'r') as f:
    data = json.load(f)
    print data
    print '\n'
    for type in data:
        #print data[type]
        del_sum = 0
        for i in range(len(data[type])):
            i = i-del_sum
            v = data[type][i]

            #print v
            info = base64.b64decode(v['TEXT'])

            if '@' in info:
                link_name = info.split(' ')[-1]
                link_name = link_name.replace('\\', '')
                post = 'https://api.pwrtelegram.xyz/user192940014:OEPPre-g-DVGT9Dx1JLrwQOUj1FPqpUq6zDZhR7Gvi8/getChat?chat_id='+link_name
            else:
                invite_link = info.split('(')[-1][:-1]
                hash_string = invite_link.split('/')[-1]
                post = 'https://api.pwrtelegram.xyz/user192940014:OEPPre-g-DVGT9Dx1JLrwQOUj1FPqpUq6zDZhR7Gvi8/messages.checkChatInvite?hash='+hash_string

            time.sleep(60)

            r = requests.post(post, json={"key": "value"})
            state = r.json()['ok']
            #state = False
            if state == False:
                print v
                #data[type][i].pop('TEXT')
                #print i
                error_des = r.json()['error_description']
                print error_des
                del data[type][i]
                del_sum = del_sum+1
    print '\n'
    print json.dumps(data)

with codecs.open('groupss.json', 'w', encoding='utf-8') as f:
	json.dump(data, f, indent=4, ensure_ascii=False)

#print data
