<p align="center">
<img src="/media/logo.png"/>
<br/>
<h3 align="center">UNSW Class Utilisation Web Scraper</h3>
<p align="center">...</p>
<h2></h2>
</p>
<br />

<p align="center">
<a href="../../issues"><img src="..." /></a>
<a href="../../pulls"><img src="https://img.shields.io/github/issues-pr/aminbeigi/UNSW-class-util-web-scraper.svg?style=flat-square" /></a>
<img src="https://img.shields.io/github/license/aminbeigi/UNSW-class-util-web-scraper?style=flat-square">
</p>

## Description
...

## Instructions
1. clone repo  
`git clone git@github.com:aminbeigi/unsw-classutil-scraper.git`
2. cd into root dir and install requirements  
`pip install -r requirements.txt`
3. install the `unswclassutil` module locally     
`pip install .` 
4. run the `unswclassutil` module with command line args      
`python -m unswclassutil comp1511 t1 ./output.json`
5. Check the output fike path folder for file

## Example
Lets find out class utilisation for course COMP6080 is term 1 using the following command `python -m unswclassutil comp6080 t1 ./output.json`.  
Output generated for above command is found in <a href="out/example_output.json">out/example_output.json</a>.

## Requirements
* Python 3.8.10+

## Contributions
Contributions are always welcome!  
Just make a [pull request](../../pulls).

## Licence
MIT license
