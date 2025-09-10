Agentic AI Chatbot — Python Software Engineer Assignment
📌 Overview

This project is a multi-level Python chatbot that integrates Large Language Models (LLMs), tool usage, and multi-step agentic reasoning.
It was developed as part of the Python Software Engineer Assignment: LLM + Agentic Thinking.

The chatbot evolves in three levels of complexity:

Level 1: LLM-only chatbot with prompt engineering

Level 2: LLM + Calculator tool integration

Level 3: Full Agentic AI with multiple tools (Calculator + Translator) and multi-step reasoning

🟢 Level 1 — LLM-Only Smart Assistant

Accepts user queries via CLI.

Uses prompt engineering to enforce step-by-step reasoning.

Refuses to solve math problems directly (hints at calculator tool instead).

✅ Example Queries:

“What are the colors in a rainbow?”

“Tell me why the sky is blue?”

“Which planet is the hottest?”

“What is 15 + 23?” ➝ chatbot refuses and suggests using calculator.

🟡 Level 2 — LLM + Basic Tool Integration

Extends Level 1 with a calculator tool.

If math is detected, chatbot calls the calculator tool instead of answering directly.

Supports basic arithmetic (add, multiply).

Gracefully fails if multiple steps are requested.

✅ Example Queries:

“What is 12 times 7?” ➝ calculator tool

“Add 45 and 30” ➝ calculator tool

“What is the capital of France?” ➝ LLM direct answer

“Multiply 9 and 8, and also tell me the capital of Japan.” ➝ fails gracefully

🔴 Level 3 — Full Agentic AI with Multi-Step Reasoning

Extends Level 2 with multi-step reasoning + memory.

Can break down queries into sub-tasks and call multiple tools in sequence.

Integrates:

Calculator ➝ addition, multiplication

Translator ➝ English ➝ German translation

✅ Example Queries:

“Translate ‘Good Morning’ into German and then multiply 5 and 6.”

“Add 10 and 20, then translate ‘Have a nice day’ into German.”

“Tell me the capital of Italy, then multiply 12 and 12.”

“Translate ‘Sunshine’ into German.”

“Add 2 and 2 and multiply 3 and 3.”

“What is the distance between Earth and Mars?” ➝ LLM direct answer
