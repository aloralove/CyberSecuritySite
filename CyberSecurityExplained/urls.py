"""CyberSecurityExplained URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.urls import path, include"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    #url(r'^app/', include('CatWebsiteApplication.urls')),
    url(r'^OperationalSecurity/', include('OperationalSecurityTab.urls')),
    url(r'^Networks/', include('NetworksTab.urls')),
    url(r'^Cryptography/', include('CryptographyTab.urls')),
    url(r'^CostBenefit/', include('CostBenefitTab.urls')),
    url(r'^Resources/', include('ResourcesTab.urls')),
    url(r'^TopFive/', include('TopFiveTab.urls')),
    url(r'^Search/', include('SearchTab.urls')),
]

urlpatterns += staticfiles_urlpatterns()