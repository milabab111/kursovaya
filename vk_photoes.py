import requests as req
from os import listdir, makedirs
from yandex_hw import YaUploader
from tqdm import tqdm

N_IMAGES = 5
SIMPLE_TOKEN = 'a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd'
#test user id: 552934290
class VK_User():
    def __init__(self, user_id, token=SIMPLE_TOKEN):
        self.url = 'https://api.vk.com/method/'
        self.user_id = user_id
        self.params = {'access_token': token, 'album_id' : 'profile', \
                          'oauth' : token, 'owner_id': user_id, 'v': '5.131', \
                              'photo_sizes': 1, 'extended': 1, 'count': 5 }
    def get_photos(self):
        photos_url = self.url + 'photos.get' #, 'items': items
        res = req.get(photos_url, params = self.params).json()
        return res['response']['items']


if __name__ == '__main__':
    user_id = input('input user\'s VK id:  ')
    vk_x = VK_User(user_id)
    photos = vk_x.get_photos()
    token = input('Input your Yandex Disk token:  ')
    print('\n')
    uploader = YaUploader(token)
    photoes_paths = []
                    
    # tqdm() usage
    for photo in tqdm(photos[:N_IMAGES]):
        photo_path = f'reserve_photoes/{user_id}'  ##директория фоток
        path_len = len(photo_path)
        makedirs(photo_path, exist_ok=True) ##создаем папку директории
        dir_list = listdir(photo_path)  ##список файлов в директории
        
        photo_url = photo['sizes'][-1]['url']
        photo_likes = str(photo['likes']['count'])
        photo_date = str(photo['date'])
        image = req.get(photo_url).content
        
        if photo_likes+'.png' in dir_list:
            name = f'{photo_likes}_{photo_date}.png'
            photo_path += f'/{photo_likes}_{photo_date}.png' 
        else:
            name = f'{photo_likes}.png'
            photo_path += f'/{photo_likes}.png'  
        
        open(photo_path, 'wb').write(image)
        photoes_paths.append(photo_path)
        
        ## Получить путь к загружаемому файлу и токен от пользователя
        result = uploader.upload(photo_path, name, user_id)
    













