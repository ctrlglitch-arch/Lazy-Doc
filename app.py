import streamlit as st
import ast
from generator import generate_doc

st.set_page_config(page_title="LazyDoc", page_icon="📝", layout="wide")

st.title("📝 LazyDoc")
st.caption("Because writing documentation is boring. Let an AST parser + Llama 3 do it for you.")

# Set up side-by-side workspace
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📥 Paste Raw Python Code")
    
    # A real-world example to initialize the text box with
    default_code = """def process_user_data(user_list, min_age=18):
    filtered_users = []
    for user in user_list:
        if user.get('age', 0) >= min_age and user.get('is_active'):
            filtered_users.append(user['email'].lower().strip())
    return list(set(filtered_users))"""
    
    raw_code = st.text_area("Python Script:", value=default_code, height=350)
    generate_btn = st.button("🚀 Generate Docs", use_container_width=True)

with col2:
    st.markdown("### 📤 Output Documentation")
    
    if generate_btn:
        with st.spinner("Analyzing and generating..."):
            try:
                tree = ast.parse(raw_code)
                func_def = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))
                func_name = func_def.name
                args = [arg.arg for arg in func_def.args.args]
                
                # Logic for Complexity
                nodes = [n for n in ast.walk(tree) if isinstance(n, (ast.If, ast.For, ast.While, ast.ExceptHandler))]
                score = len(nodes)
                complexity = "Low 🟢" if score < 3 else "Medium 🟡" if score < 7 else "High 🔴"
                
                documentation = generate_doc(func_name, args, raw_code)
                st.session_state.doc = documentation
                
                # Show Metric and Result
                st.metric("Code Complexity", complexity)
                st.code(st.session_state.doc, language="markdown")
                
                # Add Download Button
                st.download_button(
                    label="📥 Download Documentation",
                    data=st.session_state.doc,
                    file_name="documentation.md",
                    mime="text/markdown",
                )
                
            except StopIteration:
                st.error("No function definition found. Make sure your code starts with 'def'")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.info("Your markdown documentation will show up here.")