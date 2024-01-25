# Amazon price tracker 💸

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Alcatraz312/Amazon-price-tracker)

![GitHub top language](https://img.shields.io/github/languages/top/Alcatraz312/Musical-time-machine)


Get the best deals on items you have been longing to buy on Amazon! This program uses web scraping to track the prices of the of your desired items on Amazon.  It automatically sends you an email notification when the price drops below a threshold you've specified, ensuring you never miss out on great deals.

# Getting Started
 
## Prerequisites
Before using the program, you'll need the following: 
* Python 3.6 or higher installed on your system.
* 2-Step verification for your email (for Gmail and yahoo users).
* Gmail or Yahoo app.
* Your "User-Agent" and "Accept-Language" from [HTTP Headers](http://myhttpheader.com/).

## Installation
1. Clone this GitHub repository to your local machine:
```python
git clone https://github.com/Alcatraz312/Amazon-price-tracker.git
```
2. Change into the project directory:
```python
cd Amazon-price-tracker
```
3. Create a virtual python environment for your project:
```python
python -m venv environment
```
4. Activate the virtual environment\
*Linux:
```python
. <path_to_env>/bin/activate
```
*Windows (Powershell):
```python
<path_to_env>/Scripts/Activate.ps1
```
*Windows (Command prompt):
```python
<path_to_env>/Scripts/Activate.bat
```
5. Upgrade pip to the latest version:
```python
python.exe -m pip install --upgrade pip
```
6. Install the required python packages using pip:
```
pip install -r requirements.txt
```
## Configuration

To use this program, you need to set up an app password if you use Gmail or yahoo. 

1. Turn on 2-Step Verification for your email under the Security settings for your account.

![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-11-30_12-32-24-679ba2d45bb7ff0048a045ebeea58c1c.png)

2. Add an app password under your email settings.

![](https://img-c.udemycdn.com/redactor/raw/article_lecture/2022-11-30_12-32-24-4b4467d49c39915c0b9de65e0d43af98.png)

3. Copy the password and replace the values in config.py with your credentials and email service provider.

```python
email_provider = "smtp.gmail.com"  #Your email provider
email_ID = "YOUR EMAIL ID"
password = "YOUR APP PASSWORD"
```
4. Replace the values of http headers in scraping.py with your "User-Agent" and "Accept-Language" values.

```python
    headers = {
    "User-Agent" : "YOUR User-Agent",
    "Accept-Language" : "en-US,en;q=0.9"
    }                               #class attribute
```

## Usage
1. Run the script by executing the following command in the terminal: 
```
python main.py
```
2. The program will prompt you to enter the URL of your desired item from amazon. 

3. Let the program handle the tracking for you. Receive email notifications as soon as the price drops!

## Contribution
1. Fork the repository and create a new branch for your feature or bug fix.

2. Make your changes, and ensure that your code follows the PEP 8 style guide.

3. Write tests to cover your code if applicable.

4. Create a pull request with a clear description of your changes and why they are needed.

5. Your pull request will be reviewed, and once approved, it will be merged into the main branch.

## license

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Alcatraz312/Amazon-price-tracker/blob/main/LICENSE.md) file for details.

