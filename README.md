# text_data_augmentation

#Overview

This Python script is designed to process and augment datasets contained in an Excel file. The primary goal is to ensure each class within the dataset has exactly 100 rows, either by reducing the number of rows if there are more than 100, or by augmenting the dataset with synthetic data generated through word synonym replacement if there are fewer than 100 rows. The script leverages pandas for data manipulation and nlpaug for data augmentation.
Requirements

    Python 3.x
    pandas
    nlpaug
    openpyxl (for reading/writing Excel files)

#Installation

Before running the script, ensure you have the necessary libraries installed. You can install them using pip:

bash

pip install pandas nlpaug openpyxl

#Usage

    Place your Excel file in a known directory.
    Update the path/to/excel/file in the main function with the path to your Excel file.
    Update the path/to/output.xlsx in the main function with the desired output path for the augmented Excel file.
    Run the script.

#How It Works

    Load Data: The script starts by loading an Excel file into a pandas DataFrame.
    Class Separation: It then separates the data based on the class, extracting rows into individual DataFrames for each class.
    Data Reduction or Augmentation:
        If a class has more than 100 rows, it randomly drops rows until only 100 remain.
        If a class has fewer than 100 rows, it uses nlpaug to augment the data by generating new rows. This augmentation is done by replacing words in a selected text column with their synonyms.
    Recombination and Output: The modified or augmented DataFrames for each class are combined into a single DataFrame and exported to an Excel file.

#Functions
##reduz_linhas(db)

Reduces the number of rows in the DataFrame db to 100 by randomly dropping excess rows.
##augment_data(db)

Augments the DataFrame db by adding synthetic rows until it contains 100 rows. This is done through synonym replacement in a specified text column.
##main()

The main function that orchestrates the loading of the Excel file, processes each class through reduction or augmentation as needed, and then combines and exports the resulting DataFrame to a new Excel file.
#Note

The script assumes the existence of a 'Classe' column for class identification and a 'Texto Extraído' column for text that will be used for augmentation. Adjust these column names based on your dataset.
