# RandomLootGenerator v1.02

## Description

Dungeons and Dragons Random Loot generator 

This project will eventually have a random loot generator that has a fully fleshed out GUI.  Currently, this is my work on said project. 

## Prerequisites

* python 3 or greater
* node

## Installation

Create and virtual env, activate it run
> pip install -r requirement.txt

> npm install

> npm run build

> npm run start

## Usage

Navigate to localhost:5000/

Input the CR and select if it is loot from an individual or group/hoard loot.

Click `roll` and the app will roll up loot using the respective tables.

You can edit the tables being rolled on by editting the xlsx or JSON files. (if you 
edit the xlsx, you will need to run the `Converter.py` to update the JSON file)

## Built With

python
* pandas
* numpy
* flask
* flask-restful
* python-dotenv
javascript
* react
* redux
* axios

## Support

If you have any suggestions or issues, please e-mail me at phillipb1991@msn.com.

## Change Log

11/26/18 Created proof of concept that rolled on an item table from an xlsx file  
11/27/18 Added CR and type indentifiers  
01/21/19 Added a rudimentary GUI that works with CR 1-4  
01/25/19 Updated to accommodate all challenge ratings and added a section for gems and art that will be expanded upon in a future update  
04/08/19 Updated to roll each magic item and art/gem object. This is the first fully functional version  
04/09/19 Created a JSON based loot generator that is much faster than the excel based version.  An excel file and accompanying converter are included to make changing the tables easier. 
12/17/20 Pivoted to webapp with flask backend
12/31/20 Added react frontend and basic visualization
