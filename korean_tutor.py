import subprocess
import time

def run_script(file_path, use_streamlit=False):
    command = ['streamlit', 'run', file_path] if use_streamlit else ['python', file_path]
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        print(f"Successfully ran {file_path} using {'Streamlit' if use_streamlit else 'Python'}, output was:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running {file_path}: {e}\nOutput was:\n{e.stderr}")

def main():
    # Path to the Python scripts
    anki_export_script = 'P:/Program Files/Python_programs/Study App/Anki export.py'
    data_cleaning_script = 'P:/Program Files/Python_programs/Study App/Data_cleaning.py'
    chatgpt_script = 'P:/Program Files/Python_programs/Study App/chatgpt.py'
    
    # Run scripts in sequence
    print("Starting Anki export...")
    run_script(anki_export_script)
    
    time.sleep(1)
    print("Starting data cleaning...")
    run_script(data_cleaning_script)
    
    time.sleep(5)
    print("Starting chatbot interaction...")
    run_script(chatgpt_script, use_streamlit=True)
    
    print("All scripts have been executed.")

if __name__ == '__main__':
    main()
