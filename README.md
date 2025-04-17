# Study Smart Agent

> **Note:** This project is still under development and is not fully ready yet. Features and documentation may change as development progresses.

3.  **Install dependencies:**
    Use the commands listed below to setup the environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Configuration:**
    *   Make sure to configure the Environment variables in a ```.env``` file.
    *   This includes the following API Keys in .env
    ```bash
    GOOGLE_GENAI_USE_VERTEXAI=FALSE
    GOOGLE_API_KEY=YOUR_API_KEY
    ```

## Running the Agent

1.  **Navigate to the agent directory:**
    Make sure you are in the directory where ```/venv``` and ```.env``` are located. THIS IS NOT INSIDE ```/study_smart```

2.  **Run the agent using the Agent Development Kit tools:**
    There are three ways to run the agent:
    * **In your terminal:**
    ```bash
    adk run study_smart
    ```

    * **Using the built-in ADK UI:**
    ```bash
    adk web
    ```
    Once you open the web interface, you can select the agent from the dropdown menu in the top left, and interact with it through the web interface.

    * **Using a API Server (FastAPI):**
    ```bash
    adk api_server
    ```

3.  **Interact with the agent:**
    Once running, you can interact with the agent through the interface provided by the Agent Development Kit or the specified communication channels (e.g., a web interface, command line, API).
