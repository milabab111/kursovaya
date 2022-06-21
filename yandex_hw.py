import requests as req

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str, file_name, folder_name=None):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        #headers = {'Authorization': , 'Accept': 'application/json'}
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': self.token}
        upload_feedback = 'https://cloud-api.yandex.net:443/v1/disk/resources'\
            '/upload?path='
        folder_feedback = 'https://cloud-api.yandex.net:443/v1/disk/resources?path='
        if folder_name:
            folder_request = req.put(folder_feedback+folder_name, headers=headers)
            #print(folder_request.json())
            upload_url = req.get(upload_feedback+folder_name+"/"+file_name, headers=headers).json()
        else:
            upload_url = req.get(upload_feedback+file_name, headers=headers).json()
            
        #(upload_url)
        #print(upload_feedback, upload_url )
        ##Загрузка файла из file_path на upload_feedback
        upload_url = upload_url['href']
        my_response = req.put(upload_url, data=open(file_path, 'rb'))
        #print(my_response)
        


#token = 'AQAAAAA3NCA-AADLW2pny871GkK7hTUcq3j8UWk'
#uploader = YaUploader(token)
#result = uploader.upload(path_to_file)



if __name__ == '__main__':
    ## Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('path: ')
    folder_input = input('folder: ')
    file_name = input('file name: ')
    token = input('token:  ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, file_name, folder_input)
















