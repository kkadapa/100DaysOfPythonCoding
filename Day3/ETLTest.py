import csv

# Step 1: Extract - Read data from the source file
def extract_data(source_file):
    data = []
    with open(source_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


# Step 2: Transform - Perform data transformation
def transform_data(data):
    header = data[0] # Extract the header row
    transformed_data = [header] # Initialize the transformed data with the header

    for row in data[1:]:  # Skip the header row and process the data
        # For simplicity, let's assume we're adding 10 to the second column value
        transformed_row = [row[0], str(int(row[1]) + 10)]
        transformed_data.append(transformed_row)
    return transformed_data


# Step 3: Load - Write transformed data to a new CSV file
def load_data(transformed_data, target_file):
    with open(target_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(transformed_data)


if __name__ == "__main__":
    source_file = 'source_data.csv'
    target_file = 'transformed_data.csv'

    # Extract data
    extracted_data = extract_data(source_file)

    # Transform data
    transformed_data = transform_data(extracted_data)

    # Load data
    load_data(transformed_data, target_file)

    print("ETL job completed. Transformed data saved to", target_file)
