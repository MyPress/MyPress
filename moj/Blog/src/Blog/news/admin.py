# -*- coding: utf-8 -*-
from django.contrib import admin

#import pliku z modelami
from news.models import *

#rejestrujemy ka�dy model podaj�c jego nazw�
admin.site.register(Artykul)