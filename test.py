import requests

url = "https://intellisheet.azurewebsites.net/extract-text/"
files = {"pdf_file": open("./init/chat-input.pdf", "rb")}

response = requests.post(url, files=files)

# Log the response content
print("Response content:", response.content)

# Decode the response content as JSON
try:
    json_response = response.json()
    print("JSON response:", json_response)
except Exception as e:
    print("Error decoding JSON response:", e)
