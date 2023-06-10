from django.shortcuts import render
import time
import random

# Create your views here.
from django.http import HttpResponse

response = """{
    "businesses": [
        {
            "name":"Teton Elementary",
            "streetAddress":"126 Main Street",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-458-0154",
            "website":"https://sd215tet.ss4.sharpschool.com/",
            "imageURL":"./images/directory-teton-elementary.jpg",
            "membershipLevel":"nonprofit",
            "adcopy":"Teton Elementary has been around a long, long time."
        },
        {
            "name":"Teton Post Office",
            "streetAddress":"8 East Main Street",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-458-4455",
            "website":"https://tools.usps.com/find-location.htm?location=1384471",
            "imageURL":"./images/directory-post-office.jpg",
            "membershipLevel":"nonprofit",
            "adcopy":"All your postal needs in one small place."
        },
        {
            "name":"Teton 1st and 2nd Ward",
            "streetAddress":"44 East Main Street",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-458-4330",
            "website":"https://www.churchofjesuschrist.org/maps/meetinghouses/@43.887142,-111.671221,18&id=ward:187291",
            "imageURL":"./images/directory-teton-ward.jpg",
            "membershipLevel":"nonprofit",
            "adcopy":"The church of Jesus Christ - in Teton!"
        },
        {
            "name":"Ancient Grains",
            "streetAddress":"V8P8+XW",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-557-4351",
            "website":"http://ancientgrains.com/",
            "imageURL":"./images/directory-ancient-grains.jpg",
            "membershipLevel":"gold",
            "adcopy":"Nestled in southeast Idaho at the foothills of the Grand Teton mountain range, we are a family-owned and operated farm and mill committed to restoring ancient grains to the family dinner table."
        },
        {
            "name":"The Haunted Mill",
            "streetAddress":"95 Teton Hwy",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-458-2256",
            "website":"http://www.thehauntedmillinteton.com/",
            "imageURL":"./images/directory-haunted-mill.jpg",
            "membershipLevel":"silver",
            "adcopy":"The Haunted Mill is the largest attraction of its kind in Eastern Idaho. The setting is an authentic, historic flour mill, which is the scene for many local legends."
        },
        {
            "name":"Pumk-n-patch",
            "streetAddress":"260 East 1st South",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"none",
            "website":"https://pumpk-n-patch.webador.com/",
            "imageURL":"./images/directory-pumpk-n-patch.jpg",
            "membershipLevel":"bronze",
            "adcopy":"You pick pumpkins when in season."
        },
        {
            "name":"Taco Gonzalez",
            "streetAddress":"19 North Center Street",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-419-6643",
            "website":"https://www.facebook.com/tacosgonzalez208/",
            "imageURL":"./images/directory-tacos-gonzalez.jpg",
            "membershipLevel":"bronze",
            "adcopy":"You know you want tacos. Come and get them!"
        },
        {
            "name":"Shogun Crafts",
            "streetAddress":"3 West Main Street",
            "cityStateZip":"Teton, ID 83451",
            "phoneNumber":"208-458-4912",
            "website":"https://www.facebook.com/people/Sho-Gun-Crafts/100050826085977/",
            "imageURL":"./images/directory-shogun-crafts.jpg",
            "membershipLevel":"silver",
            "adcopy":"We are fabric store that has been serving the public for 10+ years. We offer services such as quilting and sewing."
        },
        {
            "name":"Teton Turf and Tree",
            "streetAddress":"4735 East Hwy 33",
            "cityStateZip":"Sugar City, ID 83448",
            "phoneNumber":"208-458-4161",
            "website":"http://www.tetonturf.com/",
            "imageURL":"./images/directory-teton-turf.jpg",
            "membershipLevel":"gold",
            "adcopy":"Growing quality sod since 1996, Teton Turf & Tree Farms is the premier Eastern Idaho sod farm supplier. Founder Kelly Baker started Teton Turf knowing that every property owner wants to take pride in a beautiful, green, healthy landscape."
        }                
    ]
}"""

headers = {
"Cross-Origin-Opener-Policy":"unsafe-none",
'Access-Control-Allow-Origin':'*',
'Access-Control-Allow-Headers':'Origin, X-Requested-With, Content-Type, Accept'
}

def index(request):
    return HttpResponse(response, content_type="application/json", headers=headers)
    