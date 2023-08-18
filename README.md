# chatBot
on)
# GPT-3.5 Chatbot using Flask

![Chatbot Demo](demo.gif)

This repository contains a simple chatbot application built using Flask and powered by the OpenAI GPT-3.5 model. The chatbot allows users to have interactive conversations and receive AI-generated responses.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Customization](#customization)
- [Important Note](#important-note)


## Prerequisites

Before you begin, ensure you have the following:

- Python 3.x installed on your system.
- An OpenAI API key. You can sign up for one on the [OpenAI website](https://beta.openai.com/signup/).

## Setup

1. **Clone or Download the Repository**: Begin by cloning or downloading this repository to your local machine.

2. **Install Dependencies**: Open a terminal window and install the required packages using pip:


3. **Configure OpenAI API Key**: Open the `app.py` file and replace the placeholder value of the `openai.api_key` variable with your actual OpenAI API key.

## Usage

1. **Run the Application**: In your terminal, navigate to the project directory and run the application:


2. **Access the Chatbot Interface**: Open your web browser and go to `http://localhost:5000` to access the chatbot interface.

3. **Interact with the Chatbot**: Type your message in the input box and click "Send". The chatbot will generate a response using the GPT-3.5 model and display it on the screen.

## API Endpoint

The chatbot also provides an API endpoint that can be used to interact with the chatbot programmatically. To use the API:

1. **Make a POST Request**: Send a POST request to `/api` with a JSON payload containing the user message:

```json
{
  "message": "Hello, chatbot!"
}

## Customization
You can customize the behavior of the chatbot by modifying the code in app.py. Experiment with different model configurations, input formats, and response handling strategies.

## Important Note
Keep in mind that the OpenAI API usage is subject to rate limits and billing. Review the OpenAI documentation for information on usage limits and pricing.
