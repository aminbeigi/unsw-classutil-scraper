<p align="center">
<img src="/media/logo.png"/>
<br/>
<h3 align="center">UNSW Class Utilisation Web Scraper</h3>
<p align="center">A script to scrape UNSW Class Utilisation web page. </p>
<h2></h2>
</p>
<br />

<p align="center">
<a href="../../issues"><img src="..."/></a>
<a href="../../pulls"><img src="https://img.shields.io/github/issues-pr/aminbeigi/unsw-classutil-scraper.svg?style=flat-square" /></a>
<img src="https://img.shields.io/github/license/aminbeigi/unsw-classutil-scraper?style=flat-square">
</p>

## Description
<a href="http://classutil.unsw.edu.au/">UNSW Class Utilisation</a> contains course capacity for all subject areas (e.g. COMP) in each term (i.e. U1/T1/T2/T3).  

unswclassutil will get all relevant rows for a specific COMP course (e.g. COMP1511), store it in JSON format and output into a specified file. Currently only scrapes subject area of COMP (computer science) but can be easily extended to scrape other subject areas aswell.

## Instructions
1. clone repo  
`git clone git@github.com:aminbeigi/unsw-classutil-scraper.git`
2. cd into root dir and install requirements  
`pip install -r requirements.txt`
3. install the `unswclassutil` module locally     
`pip install .` 
4. run the `unswclassutil` module with command line args  
`python -m unswclassutil course term output_file_path`
for example: `python -m unswclassutil comp1511 t1 ./output.json`
5. check the output JSON in the specified output file path

## Example
Lets find class utilisation for course COMP6080 in term 1 using the following command `python -m unswclassutil comp6080 t1 ./output.json`.  
Output generated for above command is found in <a href="out/example_output.json">out/example_output.json</a>.

## Requirements
* Python 3.8.10+

## Contributions
Contributions are always welcome!  
Just make a [pull request](../../pulls).

## Licence
MIT license
