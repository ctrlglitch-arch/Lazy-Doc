# LazyDoc

Nobody likes writing documentation.

LazyDoc takes Python code and generates readable documentation automatically, so you don't have to spend time explaining every function manually.

## What it does

* Reads Python code using AST
* Understands functions, classes, parameters, and structure
* Uses Groq-powered AI to generate documentation
* Shows code and generated docs side-by-side

## Tech Stack

* Python
* Streamlit
* AST
* Groq API

## Run Locally

```bash
git clone <repo-url>
cd LazyDoc
```

Create a `.env` file:

```env
GROQ_API_KEY=your_key_here
```

Install requirements:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python -m streamlit run app.py
```

## Why I Built It

I got tired of seeing documentation become the "I'll do it later" task on projects.

The code already contains most of the information needed to describe itself, so I built LazyDoc to turn that information into useful documentation automatically.

It won't replace good technical writing, but it can save a lot of time getting started.
