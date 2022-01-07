from django.shortcuts import render
from uploadimg.forms import ImageForm


import numpy as np
from PIL import Image
from feature_extractor import FeatureExtractor
from datetime import datetime
from pathlib import Path
from numpy_ml.utils.distance_metrics import manhattan,euclidean
import cv2
from sklearn.metrics.pairwise import cosine_similarity,cosine_distances
from products.models import Item
import pandas as pd


from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
import os
from pathlib import Path

fe = FeatureExtractor()
features = []
img_paths = []
for feature_path in Path("./static/feature").glob("*.npy"):
    features.append(np.load(feature_path))
    img_paths.append(feature_path.stem)
features = np.array(features)


# manhattan disitance
def distances(arr,y):
    dists = []
    for x in arr:
        dists.append(manhattan(x,y))
    return dists



# def index(request):
#     print("request.method___________________________________________________: ", request.method)
#     if request.method=="POST":
#         form=ImageForm(request.POST, request.FILES)
#         print("form.is_valid()________________________: ", form.is_valid())
#         if form.is_valid():
#             form.save()

#             img_obj=form.instance

#             # print("img_obj.image.url:_________________: ", (img_obj.image.url).split("/")[-1])

#             img = Image.open("media/images/"+str((img_obj.image.url).split("/")[-1]))
#             uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + str((img_obj.image.url).split("/")[-1])
#             query = fe.extract(img)
            
#             dists = distances(features,query)
            
#             ids = np.argsort(dists)[:30]
            
#             scores = [[dists[id], img_paths[id]] for id in ids]
#             s = []
#             try:
#                 for i,j in scores:
#                     # print("scores____i:_________________: ", str(j).split("/")[0].split("\\")[-1])
#                     s.append([i, "/media/img/"+str(str(j).split("/")[0].split("\\")[-1])])
#             except:
#                 pass
#             # print("S_213243________________: ", s)
#             # print("scores12312:_________________: ", str(s[0][1]).split("/")[0].split("\\")[-1])
#             # print("scores_43242:_________________: ", s[0][0])
#             # return render(request, 'index.html', {'form':form, 'img_obj':img_obj})
#             return render(request, 'index.html', {'form':form, 'img_obj':img_obj, 'scores':s})
#     else:
#         form=ImageForm()
#     return render(request, 'index.html', {'form': form})




# from django.shortcuts import render
# def home(request):
#     # products = Product.objects.all().filter(is_available=True)
#     # context = {
#     #     'products': products,
#     # }
#     return render(request, 'home.html')

#---------------------------------------------------------------------

def remove_img():
    dir = Path("media/images/")
    img_dir = sorted(list(map(str, list(dir.glob("*.jpg")))))
    for ad in img_dir:
        os.remove(str(ad))


def home(request):
    if request.method=="POST":
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("form.save('search_img.jpg'):", form.save("search_img.jpg"))
            img_obj=form.instance

            img = Image.open("media/images/"+str((img_obj.image.url).split("/")[-1]))
            uploaded_img_path = "static/uploaded/" + datetime.now().isoformat().replace(":", ".") + "_" + str((img_obj.image.url).split("/")[-1])
            query = fe.extract(img)
            
            dists = distances(features,query)
            
            ids = np.argsort(dists)[:30]
            scores = [img_paths[id] for id in ids]
            a = []
            try:
                for i,j in scores:
                    s.append([i, "/media/img/"+str(str(j).split("/")[0].split("\\")[-1])])
            except:
                pass
            ids = []
            df = pd.read_csv("list_id_img.csv")
            mapping = dict()
            for i in range(len(df)):
                mapping[df[i:i+1]['image'][i]]=df[i:i+1]['id'][i]
            id_img = []
            for i in scores:
                id_img.append(mapping[i+'.jpg'])
            for i in id_img:
                products = Item.objects.filter(id=i)
                for p in products:
                     a.append(p)
                     
            context = {'products':a}
            return render(request, 'home.html', {'form': form, 'scores':a})
    else:
        form=ImageForm()

    remove_img()
    return render(request, 'home.html', {'form': form})

