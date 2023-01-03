import csv

def analyze_rain(data):
  total_rain = 0
  for day in data:
    total_rain += day['rain']

  avg_rain = total_rain / len(data)

  return {
    'total_rain': total_rain,
    'avg_rain': avg_rain
  }

def print_table(results):
  print('Day\tRain (inches)')
  print('------------------')
  for result in results:
    print('{}\t{:.2f}'.format(result['day'], result['rain']))
  print()
  print('Total rain: {:.2f} inches'.format(results['total_rain']))
  print('Average daily rain: {:.2f} inches'.format(results['avg_rain']))

def main():
  # Read data from CSV file
  data = []
  with open('rain_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
      data.append(row)

  # Analyze the data
  results = analyze_rain(data)

  # Print the results in a table
  print_table(results)

if __name__ == '__main__':
  main()
