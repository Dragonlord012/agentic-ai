Here is the updated README.md. I have added a dedicated "🛠️ Tech Stack" section that explicitly details the specific packages, the Gemini 2.0 model, and the search tools you are using.

You can copy-paste this directly into your GitHub.

Markdown

#  LinkedIn Post Generator Agent

A "Strict-Mode" AI Agent that autonomously researches topics and writes viral LinkedIn posts using **Google Search** and **Gemini 2.0**.

This project uses the **Google Agent Development Kit (ADK)** to enforce a "Zero-Hallucination" policy: the agent must search the web for every request and citations are automatically extracted from the model's metadata.

---

##  Tech Stack & Components

Component,Specification,Reason for Choice
Model,gemini-2.0-flash,The fastest reasoning model available; critical for minimizing latency during the retry loops.
Framework,google-adk,"Google's Agent Development Kit provides the structured Agent, Tool, and Runner classes needed for complex orchestration."
Search Tool,Google Search,"Provides Dynamic Retrieval, allowing the model to decide what to search for (e.g., ""latest AI stats"") rather than just matching keywords."
Validation,Python grounding_chunks,We use direct metadata inspection to guarantee 100% truthful citations.
---

##  Key Features

* **🔍 Forced Grounding:** The agent is programmatically forced to use the `Google Search` tool. Responses without search metadata are automatically rejected.
* **📱 LinkedIn-Optimized:** Generates content specifically formatted for the LinkedIn feed (Hooks, Line Spacing, Hashtags).
* **🔗 Automated Bibliography:** The Python script parses `grounding_chunks` from the API response to append valid source URLs at the bottom of the post.
* **🛡️ Retry Logic:** If the model acts "lazy" (answers from memory), the script catches it and triggers a retry with stricter prompts.

---
