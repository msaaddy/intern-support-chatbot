# Intern Support AI Chatbot

## Overview

The Intern Support AI Chatbot is an NLP-based chatbot developed to answer common intern questions and provide real-time support.

The chatbot uses Rasa to understand intern queries and provide appropriate responses.

## Objective

Develop an AI chatbot to answer intern queries and provide support in real time.

## Features

- Answers common intern questions
- Understands different forms of questions
- Provides leave information
- Provides internship schedule information
- Provides supervisor information
- Provides report submission guidance
- Provides attendance information
- Provides task information
- Provides certificate information
- Provides working-hours information
- Provides feedback information
- Handles unsupported questions with a fallback response
- Uses FAQ data
- Includes historical support-ticket data
- Runs locally without a paid AI API

## Technologies Used

- Python
- Rasa
- Rasa SDK
- Natural Language Processing
- YAML
- CSV

## Data

The project includes:

- FAQ data
- Historical support tickets
- NLP training examples
- Test questions

## Project Structure

```text
intern-support-chatbot/
│
├── actions/
│   └── actions.py
│
├── data/
│   ├── faq.csv
│   ├── support_tickets.csv
│   ├── test_questions.csv
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
│
├── .gitignore
├── README.md
├── config.yml
├── credentials.yml
├── domain.yml
└── endpoints.yml