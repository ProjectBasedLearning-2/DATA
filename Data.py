import csv
import random

# Define the number of rows for the dummy data
num_rows = 1500

# Define the headers for the CSV file
headers = ['Soil Type', 'Moisture Content (%)', 'Wilting Point (%)', 'Recommended Fertilizers']

# Define the range for moisture content and wilting point for each soil type
soil_types = ['Sand', 'Loamy Sand', 'Sandy Loam', 'Loam', 'Silt Loam', 'Silty Clay Loam', 'Clay Loam', 'Sandy Clay Loam', 'Silty Clay', 'Clay']
moisture_ranges = {
    'Sand': (5, 15),
    'Loamy Sand': (10, 20),
    'Sandy Loam': (15, 25),
    'Loam': (20, 30),
    'Silt Loam': (25, 35),
    'Silty Clay Loam': (30, 40),
    'Clay Loam': (30, 40),
    'Sandy Clay Loam': (25, 35),
    'Silty Clay': (30, 40),
    'Clay': (25, 35)
}
wilting_point_ranges = {
    'Sand': (1, 8),
    'Loamy Sand': (5, 10),
    'Sandy Loam': (10, 15),
    'Loam': (12, 20),
    'Silt Loam': (15, 25),
    'Silty Clay Loam': (20, 30),
    'Clay Loam': (25, 35),
    'Sandy Clay Loam': (25, 35),
    'Silty Clay': (30, 40),
    'Clay': (35, 50)
}

# Define recommended fertilizers for each soil type
recommended_fertilizers = {
    'Sand': ['Nitrogen', 'Potassium'],
    'Loamy Sand': ['Organic Fertilizer', 'Nitrogen'],
    'Sandy Loam': ['NPK (Nitrogen, Phosphorus, Potassium)', 'Potash'],
    'Loam': ['Compost', 'Nitrogen', 'Phosphorus'],
    'Silt Loam': ['Phosphorus', 'Nitrogen', 'Potash'],
    'Silty Clay Loam': ['Potash', 'Nitrogen', 'Micro-Nutrients'],
    'Clay Loam': ['Nitrogen', 'Potassium', 'Phosphorus'],
    'Sandy Clay Loam': ['DAP (Diammonium Phosphate)', 'Nitrogen'],
    'Silty Clay': ['Micro-Nutrients', 'Potash'],
    'Clay': ['Urea', 'Potassium', 'Nitrogen']
}

# Generate dummy data
data = []
for _ in range(num_rows):
    soil_type = random.choice(soil_types)
    min_moisture, max_moisture = moisture_ranges[soil_type]
    moisture_content = round(random.uniform(min_moisture, max_moisture), 2)
    min_wilting_point, max_wilting_point = wilting_point_ranges[soil_type]
    wilting_point = round(random.uniform(min_wilting_point, max_wilting_point), 2)
    recommended_fertilizer = ', '.join(recommended_fertilizers[soil_type])
    data.append([soil_type, moisture_content, wilting_point, recommended_fertilizer])

# Write the data to a CSV file
with open('dummy_data_with_fertilizers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)

print("Dummy data with recommended fertilizers generated and saved to 'dummy_data_with_fertilizers.csv' file.")
