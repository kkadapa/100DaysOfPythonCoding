import pandas as pd

def main():
    print("Let's parse excel file ")

    # Specify the path to your CSV file
    file_path = file_path = "/Users/nathandrake/Documents/Development/Python/sampleuserids.csv"

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Access the column values
    user_ids = df["User ID"]  # Assuming the column name is "User ID"

    # Print the user IDs
    for user_id in user_ids:
        print(user_id)



if __name__ == '__main__':
    main()