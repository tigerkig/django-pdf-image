from django.shortcuts import render
from pdf2image import convert_from_path
import os
import mimetypes
import os
from django.http.response import HttpResponse

def index(request):
    if request.method == 'POST':
        url = request.POST.get('pdf_url')
        image_name = os.path.basename(url).split(".")[0] + "_first_page_image.jpg"

        images = convert_from_path(url)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filepath = BASE_DIR + '/imageFiles/' + image_name
        images[0].save(filepath, 'JPEG')

        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % image_name
        return response
    else:
        return render(request, 'index.html')
