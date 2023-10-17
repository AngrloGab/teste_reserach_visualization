import requests
import pandas as pd
import streamlit

url = "https://v1.nocodeapi.com/angelocomputacao/typeform/AArVEsnPpiiTArBx/formResponses"
params = {"formId": "UP7gO9Nu"}
r = requests.get(url = url, params = params)
result = r.json()

respostas = result['data']
dataExtract = respostas[0]['answers']
keys = list(dataExtract.keys())


valuesList = []
for resposta in respostas:
  dataExtract = resposta['answers']
  values = []
  for item in keys:
    valor = dataExtract[item]
    values.append(valor['label'])
  valuesList.append(values)

df = pd.DataFrame(valuesList, columns =keys) 

streamlit.dataframe(df)
