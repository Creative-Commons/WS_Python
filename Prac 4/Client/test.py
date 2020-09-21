from zeep import Client

url = 'http://localhost:44308/Operation.asmx?WSDL'

client = Client(url)
result = client.service.Add(100, 200)
print(result)