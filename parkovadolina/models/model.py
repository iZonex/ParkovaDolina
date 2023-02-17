import csv

class CSVModel:
    
    DB_NAME = None
    
    def read_from_db(self):
        # Open the CSV file for reading and writing
        with open(f'db/{self.DB_NAME}.csv', 'r+', newline='') as file:
            # Create a CSV reader object
            reader = csv.reader(file)
            return [row for row in reader]
        
    def write_to_db(self, data):
        with open(f'db/{self.DB_NAME}.csv', 'a') as file:

            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the new rows to the file
            writer.writerow(data)
