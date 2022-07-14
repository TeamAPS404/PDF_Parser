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

## Code Snippets

#### def get_key(element: str) -> tuple[str, str]:
This function returns the key for the element and the remaining text in the form of strings. It takes an element of type string and returns a tuple of key and text.

#### class Element(dict, Generic[T]):
It represents an element of a type string with a key parameter in the document. The main function of this class is to add all the children to the parent element.

#### def make_nested_json(elements, max_header=6, root_header="h2", drop_keys=[]) -> tuple[ list[Element], list[Element] ]:
This function turns an element array into a nested JSON array with h1 as root.

#### def fonts(doc, granularity=False):
This function is used to extract fonts and their usage in PDF documents. It takes a parameter doc which helps in iterating through the PDF document. It uses fonts flags and colors to discriminate text. It returns the most used fonts sorted by count, and font style information.

#### def font_keys(font_counts, styles):

It returns a dictionary with font sizes as keys and keys as values. It takes font size and counts as parameters and returns all element keys based on font sizes.

#### def headers_para(doc, size_key):
This function scrapes headers & paragraphs from PDF and returns texts with element keys. It also takes a doc as a parameter to iterate through the pdf.

#### def build_dict(elements):
This function takes the list of elements and builds and returns a dictionary of all the elements.

#### def main():
This function mainly used argeparse library of Python.
- Firstly, argeparse is used to get the input pdf file
- Then use it to get the max header size and root header size
- Now, the parameters are added to enable note reversal and to pass CSV of keys to drop
- Then, we get all the font counts, styles, keys, headers, and paragraphs as well as the root header and max header. 
- The drop key CSV is parsed into a list.
- Finally, all the converted JSON code is written into the JSON file of the same name as the input file in the output directory, and all the elements are added to that JSON file.


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



