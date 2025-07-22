# Fyllo Chatbase

This repository contains code for web scraping text data from a webpage and performing question answering using LangChain's tools and models. It provides scripts to extract information from a webpage and answer questions based on the extracted content using OpenAI's language models.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

The LangChain Web Scraping and Question Answering Repository is designed to showcase how to use LangChain's tools and models to perform web scraping and question answering tasks. It includes Python scripts that demonstrate how to:

- Extract text data from a webpage using [Trafilatura](https://trafilatura.github.io/).
- Split the extracted text data into smaller chunks for processing.
- Utilize LangChain's question answering chains to answer user queries based on the extracted content.

## Installation

To set up the repository and run the provided scripts, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/anirudhjain26/fyllo-chatbase.git
cd fyllo-chatbase
```

2. Create a virtual environment (recommended) and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage 

### Web Scraping and Question Answering

1. Create a `.env` file in the root directory of the repository and set your OpenAI API key:

```dotenv
OPENAI_API_KEY="sk-your_key_here"
```

Replace `your_key_here` with your actual OpenAI API key.

2. 1. Run the `websiteLoader.py` script to perform question answering and web scraping:

```bash
python websiteLoader.py
```

This script will extract information from the specified webpage and answer a predefined question using LangChain's models.

2. 2. Run the `textLoader.py` script to perform question answering:

```bash
python textLoader.py
```

This script will use text from `scrapedText.txt` and answer a predefined question using LangChain's models.

## Configuration

The repository includes the following files:

- `textLoader.py`: Demonstrates how to load text data from a file and perform question answering using LangChain's tools. Requires a valid OpenAI API key and a `.env` file.
- `websiteLoader.py`: Illustrates web scraping and question answering using LangChain's models. Scrapes live website data using `trafilatura` module. Requires a valid OpenAI API key and a `.env` file.
- `scrapedText.txt`: Contains the text data extracted from the website [https://www.fyllo.in/](https://www.fyllo.in/).
