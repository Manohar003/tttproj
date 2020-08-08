from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.template.response import TemplateResponse
import itertools
from .models import Submitnum

def homepage(request):
    return render(request=request,
                  template_name="ttthtml/home.html",
                  context={"tttsubmit":Submitnum.objects.all})

def inte(request):
          num =int(request.POST['manohar'],10)
          r = requests.get("https://terriblytinytales.com/test.txt")
          a=0
          str=r.text
          str = str.split()
          str1 = dict()
          m=dict()
          for i in str:
              if i in str1:
                  str1[i]+=1
              else:
                  str1[i]=1

          str1 = dict(sorted(str1.items(), key=lambda x: x[1], reverse=True))
          for c, j in str1.items():
              if a != num:
                  m[c] = j
                  a = a + 1
              else:
                  break
          return render(request,
                           "ttthtml/home.html",
                           {"tttfreq": m})



