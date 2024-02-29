import os

def delete_txt_files(download_folder):
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Define the relative path to the 'instagram' directory
        relative_instagram_path = os.path.join(current_directory, download_folder)

        # Convert relative path to absolute path
        instagram_directory = os.path.abspath(relative_instagram_path)

        for filename in os.listdir(instagram_directory):
            if filename.endswith(".txt"):
                file_path = os.path.join(instagram_directory, filename)
                os.remove(file_path)
                print(f"Deleted: {filename}")

        print("All .txt files in 'instagram' directory deleted successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

