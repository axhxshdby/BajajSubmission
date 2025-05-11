import requests

payload = {
    "name": "Ashish Dubey",
    "regNo": "0827CS221054",
    "email": "ashishdubey221148@acropolis.in"
}

url="https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"

response= requests.post(url, json=payload)
data = response.json()
webhook_url=data.get('webhook')
acess_token= data.get('accessToken')

sql_query="""SELECT
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM
    EMPLOYEE e1
JOIN
    DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN
    EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT AND e1.DOB > e2.DOB
GROUP BY
    e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
ORDER BY
    e1.EMP_ID DESC;"""


header = {
    'Authorization' : acess_token
    'Content-Type': 'application/json'
}
payload = {
    "finalquery" : sql_query
}

response= requests.post(webhook_url, headers=header, json=payload)