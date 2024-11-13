import os
import sys


def rename_files_with_sequential_prefix(directory):
    try:
        if not os.path.isdir(directory):
            raise FileNotFoundError(f"The directory '{directory}' does not exist.")

        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

        files.sort()

        for i, filename in enumerate(files, start=1):
            file_extension = os.path.splitext(filename)[1]
            new_name = f"file{i}{file_extension}"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{filename}' to '{new_name}'")
            except Exception as e:
                print(f"Error renaming '{filename}': {e}")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    rename_files_with_sequential_prefix(directory_path)


# ex2.py C:/Users/ASUS/Desktop/test
