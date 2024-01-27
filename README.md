# OpenAI Cheat Sheet
# Overview
This repository contains detailed notebooks to showcase the following capabilities of OpenAI:
* [Function Calling with Chat Completions API](./function_calling.ipynb)
* [Embeddings](./embeddings.ipynb)
* [Fine-Tunning](./fine_tuning.ipynb)

# Installation
This project is tested in Python 3.12.1 and openai python library 1.9.0.
## 1. Setting up the '.env' file
You need to subscribe to [OpenAI](https://platform.openai.com/docs/quickstart/account-setup), configure your [billing settings](https://platform.openai.com/account/billing/overview), get your API key and create an '.env' file containing 'OPENAI_API_KEY'.

Here is a sample '.env' file:
```
OPENAI_API_KEY=12345
```
## 2. Installing the dependencies
Open a terminal window, change your working directory to [openai-cheat-sheet](.), run the following commands. This will create and activate a virtual environment (called 'env') and install all the dependencies into it. You need to use this Python environment as the kernel, when running your Jupiter Notebooks.
```sh
    chmod +x setup.sh
    ./setup.sh
```
## 3. Getting sample data set 
When you want to run [embeddings notebook](./embeddings.ipynb), you will need [Amazon fine-food reviews dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews). Go to web site, download 'Reviews.csv' file and save under [data](./data) folder.