<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Project Data Analyst Python</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 900px; margin: auto; }
        h1, h2, h3 { color: #2c3e50; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
        code { background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
        img { max-width: 100%; height: auto; border-radius: 5px; }
        a { color: #2980b9; text-decoration: none; }
        a:hover { text-decoration: underline; }
        hr { border: 0; border-top: 1px solid #ccc; margin: 30px 0; }
    </style>
</head>
<body>

<h1>Project Data Analyst Python</h1>

<p>
    <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.13.7-blue" alt="Python Version"></a>
    <a href="https://github.com/ProjectRavel/PythonProject"><img src="https://img.shields.io/badge/github-ProjectRavel/PythonProject-lightgrey" alt="GitHub Repo"></a>
</p>

<hr>

<h2>Overview</h2>
<p>
This project documents my journey learning Python and Data Analysis. The main goal is to 
<strong>clean messy datasets and transform them into a structured format</strong>, while demonstrating my progress in using Python, Pandas, Seaborn, Matplotlib, and Jupyter Notebook.
</p>

<hr>

<h2>Installation</h2>

<h3>Step 1: Clone the repository</h3>
<pre><code>git clone https://github.com/ProjectRavel/PythonProject.git
cd PythonProject</code></pre>

<h3>Step 2: Create and activate a virtual environment (optional but recommended)</h3>
<p><strong>Windows:</strong></p>
<pre><code>python -m venv venv
venv\Scripts\activate</code></pre>

<p><strong>macOS/Linux:</strong></p>
<pre><code>python -m venv venv
source venv/bin/activate</code></pre>

<h3>Step 3: Install dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<hr>

<h2>Usage</h2>
<ol>
    <li>Open the <code>notebooks/</code> folder and select the notebook you want to run (e.g., <code>titanic_eda.ipynb</code>).</li>
    <li>Run it using VSCode or Jupyter Notebook/Lab.</li>
    <li>Analyses and visualizations will appear directly in the notebook.</li>
</ol>

<p>Example code to load the dataset:</p>
<pre><code>import pandas as pd

df = pd.read_csv("data/train.csv")
df.head()</code></pre>

<hr>

<h2>Folder Structure</h2>
<pre><code>PythonProject/
│
├─ data/                  # CSV datasets
├─ notebooks/             # Jupyter Notebooks for analysis
├─ output/                # Generated visualizations and cleaned datasets
├─ requirements.txt       # Python dependencies
└─ README.html            # Project documentation</code></pre>

<hr>

<h2>Example Visualization</h2>
<p>Example of survival rate by age group:</p>
<img src="https://raw.githubusercontent.com/ProjectRavel/PythonProject/main/output/example_survival_by_age.png" alt="Survival Rate by Age Group">
<p>Other visualizations can be found in the notebooks.</p>

<hr>

<h2>License</h2>
<p>This project is licensed under the <strong>MIT License</strong>. See the <a href="LICENSE">LICENSE</a> file for details.</p>

<hr>

<h2>Contact</h2>
<p>If you have any questions or want to collaborate:</p>
<ul>
    <li>Email: <a href="mailto:rafaelcodeid@gmail.com">rafaelcodeid@gmail.com</a></li>
    <li>GitHub: <a href="https://github.com/ProjectRavel/PythonProject">https://github.com/ProjectRavel/PythonProject</a></li>
</ul>

</body>
</html>
