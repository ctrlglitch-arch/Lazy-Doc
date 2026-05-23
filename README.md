# LazyDoc 📝

A quick tool built during a hackathon to automate the worst part of software engineering: writing documentation. 

Instead of just feeding raw text blindly to an AI, this project uses a native Python `ast` syntax tree parser to extract accurate architectural components (function shapes, parameters), merges them with the source code, and passes it to Groq's high-speed Llama 3.3 pipeline to spit out clean technical specs.

## How it works under the hood
1. **Structural Parsing:** The backend inspects the code statically via Abstract Syntax Trees (`ast`) to capture exact function bounds and signatures.
2. **Context Enrichment:** The metadata is packed into a prompt along with the raw logic.
3. **Inference Execution:** Sent through Groq API running `llama-3.3-70b-versatile` for blazing-fast documentation synthesis.
4. **UI Presentation:** Wrapped inside a simple, split-screen Streamlit dashboard.

## Setup
1. Clone this project:
```bash
   git clone <your-repo-url>
   cd crystal
