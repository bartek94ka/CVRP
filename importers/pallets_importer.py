import csv
import os

class PalletsImporter:
  def __init__(self, path):
    self.path = os.path.join(os.path.dirname(__file__), path)

  def process(self):
    pallets = []
    with open(self.path, 'rb') as file:
      reader = csv.reader(file, delimiter = ';')
      file.next()
      for row in reader:
        pallets.append({
            'typeId': int(row[0]),
            'ratioToStdPallet': float(row[1])
        })
    return pallets
