import csv  # builtin

from rest_framework.response import Response  # third-party
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError

from django.core.files.storage import FileSystemStorage  # django

from .models import Recipe  # local
from .serializers import RecipeListSerializer

data = None
file_dir = "my_csv_file_directory"
temp = "./data.csv"


def read_data(table_name):
    with open(file_dir + f'{table_name}.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        global data
        data = list(reader)
    return

def Import_csv(request):
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    csv_file = uploaded_file_url

    dbframe = cleansing(csv_file)

    for index, row in dbframe.iterrows():
        print(int(int(index) / int(dbframe.shape[0]) * 100), end='%\n')
        obj = Review.objects.create(review_content=row['Original Comment'])
        obj.save()
    return render(request, 'unit1/upload.html', {'uploaded_file_url': uploaded_file_url})


    return render(request, 'unit1/upload.html', {})


class RecipeListAPIView(generics.ListAPIView):
    """레시피 목록"""
    serializer_class = RecipeListSerializer
    queryset = Recipe.objects.all()
