# Display header for the log file analysis
print("log file Analysis")
print("=================")

# Import the sys module for accessing command line arguments
import sys

# Function to analyze a log file containing cat visit data
def analyzing_catdata(file_path):
    """  
    Analyzes a log file containing cat visit data and displays various statistics.

    Parameters:
    - file_path (str): The path to the log file containing cat visit data.
    """
     
    try:
        # Open the specified file in read mode
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"Error: File '{file_path}' not found.")
        return  
    except Exception as e:
        # Handle other exceptions (e.g., permission issues)
        print(f"Error: Unable to open '{file_path}': {e}")
        return

    # Initialize variables for statistics
    correct_cat_entries = 0
    intruding_cats_doused = 0
    total_time_correct_cat = 0
    min_duration = float('inf')
    max_duration = 0
    total_duration = 0

    # Iterate through each line in the file
    for line in lines:
        # Check for the end of the log data
        if line.strip() == 'END':
            break  
        
        # Split each line into cat type, entry time, and exit time
        cat, entry_time, exit_time = line.strip().split(',')
        entry_time, exit_time = int(entry_time), int(exit_time)

        # Check if the cat is the correct one ('OURS')
        if cat == 'OURS':
            correct_cat_entries += 1
            duration = exit_time - entry_time
            total_time_correct_cat += duration
            total_duration += duration

            # Update min and max duration values
            if duration < min_duration:
                min_duration = duration
            if duration > max_duration:
                max_duration = duration

        # Check if the cat is an intruding one ('THEIRS')
        elif cat == 'THEIRS':
            intruding_cats_doused += 1

    # Display statistics based on the log data
    if correct_cat_entries == 0:
        print("No data for the correct cat.")
    else:
        average_duration = total_time_correct_cat // correct_cat_entries
        print(f"cat visits: {correct_cat_entries}")
        print(f"other cat: {intruding_cats_doused}")
        print(f"Total time in HOURS: {total_time_correct_cat // 60} hours {total_time_correct_cat % 60} minutes")
        print(f"Average visit length: {average_duration:.2f} minutes")
        print(f"longest visit: {max_duration} minutes")
        print(f"shortest visit: {min_duration} minutes")

# Check if the script is run directly and has the correct number of command line arguments
if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Display a message if the command line argument is missing
        print("Missing command line argument! ")
    else:
        # Retrieve the file path from the command line argument and call the analysis function
        file_path = sys.argv[1]
        analyzing_catdata(file_path)