# PDF Parser

## Codefiesta project
This is a project made for Codefiesta. It is a PDF parser that can be used to parse pdf files such as FIR reports and converts it into a JSON format.

## Installation
To run this on your local system,you should have python and VS code installed. Afterwards, you need to install a python library known as PyMuPDF. With this library, we can access pdf files. Open your command window and type the following command.

```bash
pip install pymupdf
```

## How it works?
**Suppose we have a pdf file in our input folder.**
<br>

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2009_38_58.png)

<br>

 **Output would be as under in the output folder when we run our code.**
 <br>
 
 ![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2009_39_07.png)
 
 ## How to run?
 Suppose we have a file for Kerala.
 
 ![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/kerala.pdf%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_14_30.png)
 
 We want to convert it into JSON. So first we will go to our IDE(VS Code) and go to the terminal and type
 
 ```bash
python parse.py -i ./input/kerala.pdf
```

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_11_39.png)
 
The above command is written for kerala.pdf which is present inside our project in input folder. We can change the command according to the file we want to change.

After we press enter, we will see a json file created in the output folder.

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_11_53.png)
 
 Now, we can rename the JSON file as we want.

 ![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_12_10.png)
 
 




