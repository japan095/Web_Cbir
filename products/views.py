from django.shortcuts import render
from products.models import Item
from django.contrib import messages
import pandas as pd
import numpy as np
# Create your views here.
# ids=[]
# img=[]
# products = Item.objects.all()
# for p in products:
#         ids.append(p.id)
        
#         s = str(p.image)
#         img.append(s)

# ids = np.asarray(ids)
# img = np.asarray(img)

# df = pd.DataFrame({'id':ids, 'image':img})
# print(df)

# df.to_csv("list_id_img.csv")


# import pandas as pd
# import numpy as np

# data = pd.read_csv(r"D:/Mon___CongNgheMoi/Project_CK/Web_4/upload/myntradataset/styles.csv", error_bad_lines=False)

# for j in range(len(data)):
#         prod = Item()
#         prod.name = data[j:j+1]['productDisplayName'][j]
#         prod.description = str(data[j:j+1]['gender'][j]) +' | ' + str(data[j:j+1]['masterCategory'][j]) +' | ' + str(data[j:j+1]['subCategory'][j]) +' | ' + str(data[j:j+1]['articleType'][j]) +' | ' + str(data[j:j+1]['baseColour'][j]) +' | ' + str(data[j:j+1]['season'][j]) +' | ' + str(data[j:j+1]['year'][j]) +' | ' + str(data[j:j+1]['usage'][j])
#         prod.price = np.round(np.random.uniform(10,50000,1),1)[0]
#         prod.image = str(data[j:j+1]['id'][j]) + '.jpg'
#         prod.save()
#         print("prob____________________: ")
#         # print("prob____________________: ", prod.description)
#         # print("prob____________________: ", prod.price)
#         # print("prob____________________: ", prod.image)

        # break






def addProduct(request):
    if request.method == "POST":
        prod = Item()
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')

        if len(request.FILES) != 0:
            prod.image = request.FILES['image']

        prod.save()
        messages.success(request, "Product Added Successfully")
        return render(request, 'add.html')
    return render(request, 'add.html')






def editProduct(request, pk):
    prod = Item.objects.get(id=pk)

    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(prod.image) > 0:
                os.remove(prod.image.path)
            prod.image = request.FILES['image']
        prod.name = request.POST.get('name')
        prod.description = request.POST.get('description')
        prod.price = request.POST.get('price')
        prod.save()
        messages.success(request, "Product Updated Successfully")
        return redirect('/')

    context = {'prod':prod}
    return render(request, 'edit.html', context)