import requests
import ujson as json
import sys
import binascii

to_address = "KgeyPZpdecuGCeZgxv3uzgB4iEs3CvVECi5kjRoAPaTt6XxLX8BYpVKWLvHJV9AMXt9A88vtsq2QmJJc6bPQsKNJ8W5kZ1g"
content = """
 ______________
|              |
|_________/    | 
       / /|    |
      / / |    |
     / / /|    |
    / / / |    |
   / / /  |____|

def rpc(method, params={}):
    base_url = "http://localhost:8070/json_rpc"
    payload = {
        "password": "80085",
        "jsonrpc" : "2.0",
        "method" : method,
        "params" : params,
        "id" : "blah"
    }

    try:
        response = requests.post(base_url, data=json.dumps(payload)).json()
    except Exception as e:
        print("Doesn't seem like kaasu-service is running. {}".format(response))
        sys.exit(1)

    if 'error' in response:
        print("Failed to talk to server. {}".format(response))
        sys.exit(1)
    return response

r = rpc("sendTransaction", {
    "transfers": [{
        "amount": 1,
        "address": to_address,
    }],
    "fee": 10,
    "anonymity": 7,
    "extra": binascii.hexlify(content.encode()).decode()
})
print(r)
