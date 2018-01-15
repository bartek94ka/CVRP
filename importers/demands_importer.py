import csv
import os
import math

class DemandsImporter:
  def __init__(self, path):
    self.path = os.path.join(os.path.dirname(__file__), path)

  def process(self, cities, pallets):
    MAX_CAPACITY = 30 # to-do remove harcoded value
    self.pallete_type_id = [0 for x in range(len(cities))]
    self.demands = [0 for x in range(len(cities))]
    with open(self.path, 'rb') as file:
      reader = csv.reader(file, delimiter = ';')
      file.next()
      for row in reader:
        try:
          self.pallete_type_id[cities.index(row[0])] += int(row[2])
          if(self.pallete_type_id[cities.index(row[0])] == pallets[0]["typeId"]):
            self.demands[cities.index(row[0])] += int(math.ceil(int(row[1]) * pallets[0]["ratioToStdPallet"]))
          if(self.pallete_type_id[cities.index(row[0])] == pallets[1]["typeId"]):
            self.demands[cities.index(row[0])] += int(math.ceil(int(row[1]) * pallets[1]["ratioToStdPallet"]))

        except (ValueError,IndexError):
          None
      for i in range(len(self.demands)):
        if self.demands[i] > MAX_CAPACITY:
          count = self.demands[i] / MAX_CAPACITY
          originalName = cities[i]
          cities[i] = originalName + '#0'
          self.demands[i] = self.demands[i] % MAX_CAPACITY
          for j in range(count):
            name = originalName + '#' + str(j + 1)
            cities.append(name)
            self.demands.append(MAX_CAPACITY)

    return {
      'demands': self.demands,
      'cities': cities,
      'palletTypeId': self.pallete_type_id
    }
