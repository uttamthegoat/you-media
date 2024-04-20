# Creating and Using a Virtual Environment in Python

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to work on a Python project without affecting the global Python installation or other projects.

## Prerequisites

Before you begin, ensure you have Python installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

## Instructions

1. **Open your terminal or command prompt.**

2. **Navigate to the directory where you want to create the virtual environment:**

    ```bash
    cd /path/to/your/directory
    ```

3. **Create a virtual environment using the `venv` module:**

    ```bash
    python -m venv myenv
    ```

    Replace `myenv` with the desired name for your virtual environment.

4. **Activate the virtual environment:**

    - On Windows:
    
        ```bash
        myenv\Scripts\activate
        ```
        
    - On macOS and Linux:
    
        ```bash
        source myenv/bin/activate
        ```

5. **Once activated, you'll see the name of the virtual environment in your terminal prompt. Now, any Python packages you install using pip will be isolated to this virtual environment.**

6. **Once activated, you'll see the name of the virtual environment in your terminal prompt. Now, any Python packages you install using pip will be isolated to this virtual environment.**

    - To install packages listed in a `requirements.txt` file, you can use the following command:

        ```bash
        pip install -r requirements.txt
        ```

7.**Then run the script**

    - run this command in the terminal

        ```bash
        flask run
        ```


7. **To deactivate the virtual environment and return to your global Python environment, simply run:**

    ```bash
    deactivate
    ```

