import subprocess
import re
import os
import shutil

def run_magick_identify(image_path, format_string="%[parameters]"):
    try:
        cmd = f'magick identify -format "{format_string}" -verbose "{image_path}"'
        result = subprocess.check_output(cmd, shell=True, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return None

def copy_and_rename_image(image_path, new_name, output_folder):
    try:
        # Check if the image file exists
        if os.path.exists(image_path):
            # Create the output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)

            # Build the new path in the output folder
            new_path = os.path.join(output_folder, new_name)

            # Copy and rename the file
            shutil.copy(image_path, new_path)

            print(f'Copied and renamed "{image_path}" to "{new_path}"')
        else:
            print(f'File "{image_path}" does not exist.')

    except Exception as e:
        print(f"Error: {e}")

def process_files_in_folder(input_folder, output_folder):
    feelings = ["admiration", "amusement", "anger", "annoyance", "approval", "caring", "confusion", "curiosity", "desire", "disappointment", "disapproval", "disgust", "embarrassment", "excitement", "fear", "gratitude", "grief", "joy", "love", "nervousness", "neutral", "optimism", "pride", "realization", "relief", "remorse", "sadness", "surprise"]

    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".png"):
                image_path = os.path.join(root, file)
                format_string = "%[parameters]"
                result_string = run_magick_identify(image_path, format_string)

                for feeling in feelings:
                    if feeling in result_string:
                        copy_and_rename_image(image_path, f"{feeling}.png", output_folder)

if __name__ == "__main__":
    input_folder = "input"  # Replace with the path to your subfolder
    output_folder = "output"  # Replace with the path to your output subfolder
    process_files_in_folder(input_folder, output_folder)
