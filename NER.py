import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Long meaningful NLP text
text = """
Artificial Intelligence has rapidly transformed modern technology.
In 2023, OpenAI released advanced AI models such as GPT-4, which gained
global attention for their ability to understand and generate human language.
Sam Altman, the CEO of OpenAI, announced partnerships with companies like
Microsoft, investing over 10 billion dollars in AI research and infrastructure.
Major technology companies such as Google, Amazon, and Meta are also heavily
investing in AI-powered solutions.
In India, organizations like ISRO and IIT Delhi are using AI for space research
and academic innovation.
The United Nations has raised concerns about the ethical use of AI and data privacy.
On January 15, 2024, a global AI summit was held in Davos, Switzerland.
"""

doc = nlp(text)

# ENTITY COLORS (same as your code)
ENTITY_COLORS = {
    "PERSON": "#7aecec",
    "ORG": "#bfeeb7",
    "GPE": "#feca74",
    "LOC": "#ffb347",
    "NORP": "#aa9cfc",
    "DATE": "#ff9561",
    "TIME": "#ffadad",
    "MONEY": "#ffd700",
    "QUANTITY": "#d4a5a5",
    "PERCENT": "#ffcccb",
    "CARDINAL": "#cdb4db",
    "PRODUCT": "#caffbf",
    "WORK_OF_ART": "#fdffb6",
    "LAW": "#bdb2ff",
    "EVENT": "#ffc6ff",
    "FAC": "#a0c4ff",
    "LANGUAGE": "#9bf6ff",
    "ORDINAL": "#eaeaea"
}

# ---------- HTML TEXT GENERATION ----------
html_content = ""

for token in doc:
    if token.ent_type_ in ENTITY_COLORS:
        html_content += f"""
        <span class="entity" style="background:{ENTITY_COLORS[token.ent_type_]};">
            {token.text}
            <span class="label">{token.ent_type_}</span>
        </span>
        """
    else:
        html_content += token.text + " "

# ---------- FULL HTML PAGE ----------
html_page = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>NER Visualization</title>

<style>
body {{
    font-family: Arial, sans-serif;
    padding: 20px;
}}

.entity {{
    padding: 4px 6px;
    margin: 2px;
    border-radius: 6px;
    display: inline-block;
}}

.label {{
    font-size: 10px;
    background: black;
    color: white;
    padding: 2px 4px;
    border-radius: 4px;
    margin-left: 4px;
}}

.legend {{
    display: grid;
    grid-template-columns: repeat(5, auto);
    gap: 10px;
    margin-bottom: 15px;
}}

.legend-item {{
    display: flex;
    align-items: center;
    gap: 6px;
}}

.box {{
    width: 14px;
    height: 14px;
    border-radius: 4px;
}}
</style>
</head>

<body>

<h2>Named Entity Recognition (spaCy)</h2>

<div class="legend">
    {''.join([f'<div class="legend-item"><div class="box" style="background:{c}"></div>{l}</div>' for l, c in ENTITY_COLORS.items()])}
</div>

<hr>

<div>
{html_content}
</div>

</body>
</html>
"""

# Save file
with open("ner_output.html", "w", encoding="utf-8") as f:
    f.write(html_page)

print("✅ NER HTML file generated: ner_output.html")
