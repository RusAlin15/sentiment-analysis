# Text Analysis and Visualization

This Python code is designed for text analysis and visualization. 
It includes functions to read text from files, 
spit a book into chapters or analyze a diary, analyze sentiment, and create line charts to visualize sentiment data.



## Prerequisites
Before running the script, make sure you have the following prerequisites installed:

<ul>
<li>Python 3.9</li>
<li>The required Python libraries, which can be installed using pip:</li>
<li>glob for file path handling</li>
<li>re for regular expressions</li>
<li>LanguageProcessing for text sentiment analysis and visualization (please ensure you have this library or module)</li>
</ul>s

## Usage

Place the text file you want to analyze (e.g., miracle_in_the_andes.txt) in the same directory as the script.

Optionally, place your diary text files in a directory named diary within the same directory as the script.

Run the script using the following command:
```
streamlit run .\main.py
```

The script will read and analyze the text data, split it into chapters, and generate line charts to visualize the sentiment data.

## Customization

To customize the book chapter splitting pattern, modify the pattern parameter in the get_chapters function.

To change the text files to be analyzed, update the file paths in the get_from_diary and handler functions.

To customize the chart titles, modify the strings passed to the graph_representation method.
