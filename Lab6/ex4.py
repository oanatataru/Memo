import os
import sys
from collections import defaultdict


def count_files_by_extension(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        extension_counts = defaultdict(int)

        files = os.listdir(directory)
        if not files:
            print(f"The directory '{directory}' is empty.")
            return

        for file in files:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                _, extension = os.path.splitext(file)
                extension_counts[extension] += 1

        print("File counts by extension:")
        for extension, count in extension_counts.items():
            ext_display = extension if extension else "No Extension"
            print(f"{ext_display}: {count}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError:
        print(f"Permission denied to access '{directory}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    count_files_by_extension(directory_path)


# ex4.py C:/Users/ASUS/Desktop/test