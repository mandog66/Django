import os, csv, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings')
django.setup()

from mysite.models import csv_data

with open("csv/data1.csv", "r", encoding="utf-8-sig") as fp:
    csvdata = csv.DictReader(fp)
    data = [item for item in csvdata]

for item in data:
    if len(csv_data.objects.filter(name=item['name'].strip())) == 0:
        rec = csv_data(name = item['name'],
                       _id = item['id'],
                       sex = (True if item['sex'] == "M" else False),
                       num = item['num'])
        rec.save()
print("Done")