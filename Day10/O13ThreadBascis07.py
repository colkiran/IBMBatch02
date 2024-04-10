
import time
import requests
import concurrent.futures

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

st = time.perf_counter()
path = "C:\\Training\\PycharmProjects\\IBMBatch02\\Day10\\ImgFiles\\"

def ImageDownload(img_url):
    imgBytes = requests.get(img_url).content
    img_name = img_url.split("/")[3]
    imgName = f"{img_name}.jpg"
    with open(path+imgName, "wb") as FW:
        FW.write(imgBytes)
        print(f"{imgName} sucessfully downloaded........")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(ImageDownload, img_urls)

et = time.perf_counter()
print(f"The total time taken is {round(et - st, 2)} seconds")