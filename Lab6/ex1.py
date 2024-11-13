import os
import sys


def read_files_in_directory(directory, file_extension):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            print(f"\nContents of '{file_path}':\n")
                            print(f.read())
                    except Exception as e:
                        print(f"Error reading file '{file_path}': {e}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    if not file_extension.startswith("."):
        print("Invalid file extension format. Please include the dot (e.g., '.txt').")
        sys.exit(1)

    read_files_in_directory(directory_path, file_extension)


#python ex1.py C:/Users/ASUS/Desktop/test .txt
