from django.contrib import admin

import os
#print(os.getcwd())
#os.chdir(r'C:\mywork\venv\src\products')
from .models import Product


admin.site.register(Product)
