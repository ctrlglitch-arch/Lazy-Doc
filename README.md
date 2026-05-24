LazyDoc 📝
Let’s be honest: nobody actually likes writing documentation. It is the task that gets pushed to the end of the sprint, leading to code debt where nobody understands how the functions work six months later.

I built LazyDoc to stop that. It is a tool that takes your raw Python code and turns it into clean, readable documentation in seconds.

The Approach
Most tools just throw code at an AI and hope for the best. LazyDoc does it differently. I wanted the output to be accurate, not just pretty, so I built a pipeline:

Static Analysis: The backend uses Python’s ast library to scan your code structure before anything else happens. It identifies exactly what your functions are doing and what arguments they take.

Context-Aware Docs: By combining that structural data with your actual logic, the AI does not have to guess—it knows exactly what it is documenting.

Speed: I am using the Groq API (Llama 3.3) because it is fast. If you are documenting code, you do not want to be waiting around.

No-Nonsense UI: The interface is built in Streamlit. It is split-screen: your code on the left, your docs on the right. You can even check your code complexity and download the output as a Markdown file.

How to run it
Get the code:
git clone 
cd crystal

Setup:
You will need a Groq API key for this to work. Create a file named .env in the folder and put your key in there:
GROQ_API_KEY=your_key_here

Install the requirements:
pip install -r requirements.txt

Start it up:
python -m streamlit run app.py

Why this is useful
Documentation is usually the unpaid debt of every engineering team. LazyDoc does not just summarize—it provides a consistent, professional spec so you can actually onboard new people without spending hours explaining your functions.
