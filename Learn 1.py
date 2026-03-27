import requests
import json

url="http://localhost:11434/api/generate"
data={
    "model":"phi3:3.8b",
        "prompt":"Top teams in Indian Premier League"
}
response=requests.post(url,json=data,stream=True)


if response.status_code==200:
    print("The Answer is :",end="",flush=True)
    for line in response.iter_lines():
        if line:
            decoded=line.decode("utf-8")
            complete=json.loads(decoded)

            if complete.get("done"):
                break

            result=complete.get("response","")
            print(result,end="",flush=True)
else:
    print("Error Occurred,",response.status_code,response.text)

