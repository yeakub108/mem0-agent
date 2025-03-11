# Mem0 Agent - Memory-Powered AI Assistant

This project demonstrates how to build an AI assistant with memory capabilities using the Mem0 library, OpenAI, and Supabase for authentication and vector storage.

The Live Agent Studio integration verison referenced below also shows how to integrate Mem0 with a Pydantic AI agent.

## Features

- **🧠 Long-term Memory**: The AI remembers past conversations and preferences
- **🔒 Secure Authentication**: User data is protected with Supabase authentication
- **💬 Personalized Responses**: Get responses tailored to your history and context
- **🌐 Streamlit Interface**: Easy-to-use web interface for chatting with the AI

## Project Structure

This repository contains multiple implementations of the Mem0 agent:

1. **Basic Implementation** (`iterations/v1-basic-mem0.py`): Simple implementation using in-memory storage
2. **Supabase Integration** (`iterations/v2-supabase-mem0.py`): Enhanced implementation with Supabase vector storage
3. **Streamlit Web Interface** (`iterations/v3-streamlit-supabase-mem0.py`): Basic Streamlit web application with Supabase authentication for mem0 user IDs
4. **Live Agent Studio Integration** (`studio-integration-version/`): Code for integrating with Live Agent Studio

The `studio-integration-version` folder contains the code used to integrate this agent into the Live Agent Studio, including:
- API endpoint setup
- Database integration
- Authentication handling
- Message history management

## Prerequisites

- Python 3.11+
- OpenAI API key
- Supabase account and project

## Setup Instructions

1. **Create and activate a virtual environment**:
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Copy the `.env.example` file to `.env` and fill in your API keys:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `MODEL_CHOICE`: The OpenAI model to use (defaults to gpt-4o-mini)
   - `DATABASE_URL`: Your Supabase PostgreSQL connection string
   - `SUPABASE_URL`: Your Supabase project URL
   - `SUPABASE_KEY`: Your Supabase service role key

4. **Run the application**:
   ```bash
   streamlit run iterations/v3-streamlit-supabase-mem0.py
   ```

## Supabase Setup

1. Create a Supabase account and project at [supabase.com](https://supabase.com)
2. Get your Database URL from: Project Settings > Database
3. Get your API keys from: Project Settings > API
4. Enable Email Auth in: Authentication > Providers > Email

## How It Works

The application uses:
- **Mem0**: For memory management and retrieval
- **OpenAI**: For generating AI responses
- **Supabase**: For authentication and vector storage
- **Streamlit**: For the web interface

When a user sends a message, the system:
1. Retrieves relevant memories based on the query
2. Includes these memories in the prompt to OpenAI
3. Stores the conversation as a new memory
4. Displays the response to the user

## Studio Integration

The `studio-integration-version` folder contains everything needed to deploy this agent to the Live Agent Studio:

- `mem0_agent.py`: Core agent implementation
- `mem0_agent_endpoint.py`: FastAPI endpoint for the agent
- `Dockerfile`: Container configuration for deployment
- `.env.example`: Template for required environment variables

## Troubleshooting

1. **Authentication Issues**:
   - Verify your Supabase credentials are correctly set in the `.env` file
   - Check if your Supabase project has Email Auth enabled

2. **Database Connection Issues**:
   - Verify your DATABASE_URL is correctly formatted
   - Make sure you aren't using special characters in your database password. See the note in `.env.example`.
