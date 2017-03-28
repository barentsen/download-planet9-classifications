"""This will create a file called `classification-dump.txt`
containing ALL the planet9 zooniverse classifications.

You can then use this file as follows:

lines = open('classification-dump.txt', 'r').readlines()
for line in lines:
    js = json.loads(line)
"""
import json
from panoptes_client import Panoptes, Classification

PANOPTES_USERNAME = ''
PANOPTES_PASSWORD = ''

PLANET9_PROJECT_ID = 4115
OUTPUT_FN = 'classification-dump.txt'

if __name__ == '__main__':
    output = open(OUTPUT_FN, 'w')
    Panoptes.connect(username=PANOPTES_USERNAME, password=PANOPTES_PASSWORD)
    query = Classification.where(project_id=PLANET9_PROJECT_ID, scope='project')
    for i in range(5):
        classification = query.next()
        output.write(json.dumps(classification.raw) + '\n')
        output.flush()
    output.close()
