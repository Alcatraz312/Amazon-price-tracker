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
3. Install the required python packages using pip:
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

![image info](C:\Users\ratho\OneDrive\Pictures\Screenshots\Screenshot 2024-01-23 122213.png)

