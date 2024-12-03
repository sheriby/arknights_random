import os
import json
import requests

with open('person.json', 'r', encoding='utf-8') as f:
    image_urls = json.load(f)

save_dir = 'pic'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

for new_filename, img_url in image_urls.items():
    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()  # 如果请求失败，抛出异常

        file_extension = img_url.split('.')[-1]

        save_path = os.path.join(save_dir, f'{new_filename}.{file_extension}')

        with open(save_path, 'wb') as img_file:
            for chunk in response.iter_content(chunk_size=8192):
                img_file.write(chunk)

        print(f"图片 '{new_filename}' 已保存至 {save_path}")

    except Exception as e:
        print(f"下载图片 '{new_filename}' 失败: {e}")

