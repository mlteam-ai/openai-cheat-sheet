# OpenAI Cheat Sheet
# Overview
This repository contains detailed notebooks to showcase the following capabilities of OpenAI:
* [Function Calling with Chat Completions API](./01_function_calling.ipynb)
* [Embeddings](./02_embeddings.ipynb)
* [Fine-Tuning](./03_fine_tuning.ipynb)
* [Image Generation](./04_image_generation.ipynb)
* [Image Processing](./05_image_processing.ipynb)
* [Text to Speech](./06_text_to_speech.ipynb)
* [Speech to Text](./07_speech_to_text.ipynb)
* [Moderation](./08_moderation.ipynb)
* [Assistants](./09_assistants.ipynb) and [Tools](./10_assistant_tools.ipynb) that you can use with Assistants
    * Code Interpreter
    * Knowledge Retrieval
    * Function Calling
* [Evaluation framework of OpenAI](./11_evals.ipynb)

# Installation
This project is tested in Python 3.12.1 and openai python library 1.11.0.

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