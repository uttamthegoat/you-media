import os
from flask import jsonify, render_template

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



def try_except_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            # Call the original function with provided arguments
            return func(*args, **kwargs)
        except Exception as e:
            # Handle the exception here
            # error_message=f"An error occurred: {e}"
            # Optionally, you can raise the exception again to propagate it
            # return jsonify({"error": error_message}), 500
            error_message = f"An error occurred: {str(e)}"
            return render_template("result.html", success=False, error_message=error_message)
    return wrapper
