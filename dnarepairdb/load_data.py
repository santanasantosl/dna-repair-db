import os
import re
import json
import django
django.setup()
from django.conf import settings


def load_data(json_file):

    json_data = json.load(open(json_file))
    json_data_list = json_data[json_data.keys()[0]]
    print json_data_list


if __name__ == "__main__":

    json_file = os.path.join(settings.MEDIA_ROOT, 'repair.json')
    load_data(json_file)