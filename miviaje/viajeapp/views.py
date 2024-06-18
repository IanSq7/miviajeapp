from django.http import HttpResponse
from django.shortcuts import render
from django.http import response

from miviaje import settings
# Create your views here.


def hello(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=2.0">
        <title>Bienvenido a Mi Viaje App</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                text-align: center;
                flex-direction: column;
                background-image: url('https://www.mitsubishi-motors.com.pe/blog/wp-content/uploads/2021/05/aspectos-debes-preocuparte-viajar-carretera.jpg');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                color: white;
            }
            h1 {
                margin: 0;
                font-size: 3em;
                font-family: Arial, sans-serif;
                text-shadow: 2px 2px 2px rgba(0, 0, 0, 0.5);
            }
            h2 {
                margin: 0;
                font-size: 2em;
                font-family: Arial, sans-serif;
                text-shadow: 1px 1px 1px rgba(0, 0, 0, 0.5);
            }
        </style>
    </head>
    <body>
        <h1>Bienvenido</h1>
        <h2>Mi Viaje App</h2>
    </body>
    </html>
    """
    return HttpResponse(html_content)