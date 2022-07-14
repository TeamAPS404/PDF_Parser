# PDF Parser

## Codefiesta project
This is a project made for Codefiesta. It is a PDF parser that can be used to parse pdf files such as FIR reports and converts it into a JSON format.
A PDF parser, or PDF scraper, is a tool that extracts data from PDF documents.

## Problem Statement
The Indian government gets more than a million FIR pdf files each year. To accomplish this, they usually assign data extraction duties to officers who are currently on duty. The whole process is time-consuming and requires much effort. To solve this problem, we present a PDF parser. To address this issue, we have developed a PDF parser.

Extracting data from PDF documents is done by using a tool known as a PDF parser or scraper. Manual data entry (copy and paste) is the most typical approach when several documents need to be analyzed.

## Installation
To run this on your local system, you should have python and VS code installed.
Now, you need to clone this repository, go to your command line and type

```bash
git clone https://github.com/TeamAPS404/PDF_Parser.git
```

The above command is used if you want to clone via HTTPS. You may do it with SSH or Github CLI as you want.

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/Meet%20-%20rak-jeum-fyv%20and%2011%20more%20pages%20-%20Personal%20-%20Microsoft%E2%80%8B%20Edge%2014-07-2022%2011_04_22%20(2).png)


After cloning, you need to install a python library known as PyMuPDF. With this library, we can access pdf files. Open your command window and type the following command.

```bash
pip install pymupdf
```

## Example
**Suppose we have a pdf file in our input folder.**
<br>

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2009_38_58.png)

<br>

 **Output would be as under in the output folder when we run our code.**
 <br>
 
 ![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/haryana.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2009_39_07.png)
 
 ## Use case
 Suppose we have a file for Kerala.
 
 ![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/kerala.pdf%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_14_30.png)
 
 We want to convert it into JSON. So first we will go to our IDE(VS Code) and go to the terminal and write
 
 ```bash
python parse.py --input=input/<file-name>.pdf --max=8 --root="h1"
```

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/parse.py%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_37_06.png)
 
The above command is written for kerala.pdf which is present inside our project in input folder. We can change the command according to the file we want to change.

After we press enter, we will see a json file created in the output folder.

![alt text](https://github.com/TeamAPS404/PDF_Parser/blob/main/images/kerala.json%20-%20PDF_Parser%20-%20Visual%20Studio%20Code%2014-07-2022%2010_39_35.png)
 
 This output JSON will have same name as pdf.



