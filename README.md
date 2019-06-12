# Text to GUI transformer

This is a desktop application that uses regular-expressions and PyQt5 to transform a text file that contains text written in a specific pattern into a graphical user interface that consists of multiple pages and sections based on the text file pattern.

I used the application as a learning tool to present notes about the different git commands. I added some functionality to the GUI such as accelerator keys to jump faster between the different pages, and copy-on-click to copy the commands.


<p align="center">
  <img src="https://user-images.githubusercontent.com/42389687/59371566-aca0f400-8d45-11e9-9c60-467c71469984.PNG">
</p>

### Running the application locally:
-  [Python3.7](https://www.python.org/downloads/) or higher is required.
- Clone/download the repsitory and `cd` into it.
- Install external dependencies: `pip3 install -r requirements.txt`
- Run the app: `python app.py`

Take a look at notes.txt to see the pattern used, then feel free to change the application to present your own notes.
