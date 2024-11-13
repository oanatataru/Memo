import os
import sys


def calculate_total_size(directory):
    total_size = 0

    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    total_size += os.path.getsize(file_path)
                except OSError as e:
                    print(f"Could not access '{file_path}': {e}")

        print(f"Total size of all files in '{directory}': {total_size} bytes")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    calculate_total_size(directory_path)



# ex3.py C:/Users/ASUS/Desktop/test