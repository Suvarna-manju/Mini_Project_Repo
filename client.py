import requests
def upload_file(file_path):
    url='http://127.0.0.1:5000/upload'
    with open(file_path,'rb') as file:
        files ={'file':file}
        response=requests.post(url,files=files)
        print(response.json())
if __name__ == '__main__':
    file_path="C:\\Users\\ADMIN\\Downloads\\Resume CHAKALI HARITHA (1).pdf"
    upload_file(file_path)

