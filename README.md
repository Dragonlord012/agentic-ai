#  LinkedIn Post Generator Agent

A "Strict-Mode" AI Agent that autonomously researches topics and writes viral LinkedIn posts using **Google Search** and **Gemini 2.0**.

This project uses the **Google Agent Development Kit (ADK)** to enforce a "Zero-Hallucination" policy: the agent must search the web for every request and citations are automatically extracted from the model's metadata.

---

## Tech Stack & Components

Core Components

Python 3.10+: The primary programming language used for the agent's logic, API orchestration, and strict validation scripts.

Google Agent Development Kit (ADK): The framework that powers the agent's architecture. We use google-adk to define the Agent personas, manage Tool connections, and handle the execution runner loop.

Gemini 2.0 Flash: The specific AI model selected for this project (gemini-2.0-flash). It was chosen for its sub-second latency and high-reasoning capabilities, which are critical for maintaining a smooth user experience during the automated retry loops.

Tooling & Security

Google Search Tool: Enables Dynamic Retrieval. Unlike standard RAG (Retrieval-Augmented Generation), this tool allows the model to autonomously decide when and what to search for on the live web to answer the user's specific request.

Custom Grounding Validation: A specialized Python logic layer that physically inspects the grounding_metadata returned by the API. It ensures that no response is accepted unless it contains valid, clickable source links.

Python-Dotenv: A security utility used to load the GOOGLE_API_KEY from a local .env file, ensuring credentials are never hardcoded into the source code
---

##  Key Features

* Forced Grounding: The agent is programmatically forced to use the `Google Search` tool. Responses without search metadata are automatically rejected.
* LinkedIn-Optimized: Generates content specifically formatted for the LinkedIn feed (Hooks, Line Spacing, Hashtags).
* Automated Bibliography: The Python script parses `grounding_chunks` from the API response to append valid source URLs at the bottom of the post.
* Retry Logic: If the model acts "lazy" (answers from memory), the script catches it and triggers a retry with stricter prompts.

---
