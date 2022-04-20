# Access the nested key ‘salary’ from the following JSON

import json
a= """{"company":{"employee":{"name":"emma","payble":{"salary":7000,"bonus":800}}}}"""
b= json.loads(a)
print(b["company"]["employee"]["payble"]["salary"])

import json
with open("Extra.json","w") as f:
    json.dump(b["company"]["employee"]["payble"]["salary"],f)
    