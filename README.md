# 🕹️ Lore-Master OS: Gamyopedia

An AI-powered web app that generates rich video game lore, storylines, and world-building content in customizable styles and formats — powered by LLaMA via HuggingFace.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.x-green?style=flat-square)
![Model](https://img.shields.io/badge/Model-LLaMA--3.1--8B-purple?style=flat-square)

---

## 🚀 Demo

> *Screenshots coming soon — run the app to see it in action!*

---

## ✨ Features

- 🎮 Select from a dataset of games or type in any game title
- 🎙️ 9 unique narrator voice packs (Gritty Veteran, Sarcastic Robot, RPG Quest Giver, and more)
- 🌫️ Adjustable lore depth — from a quick "Vibe Check" to full "Completionist" deep dives
- 🛡️ Spoiler shield — control how much of the story gets revealed
- 🎯 Multi-focus skill tree — target Main Plot, Character Backstory, World Building, Hidden Secrets, and more
- 📤 Multiple output formats — Story, Bullet Points, Radio Log, or Poem
- ♾️ Iterative generation with seamless continuation for long-form content

---

## 🛠️ Tech Stack

| Layer | Tool |
|-------|------|
| Frontend | Streamlit |
| LLM | Meta LLaMA 3.1 8B Instruct (via HuggingFace) |
| LLM Framework | LangChain (`langchain_huggingface`) |
| Prompt Management | LangChain `load_prompt` / JSON template |
| Dataset | Custom `games.csv` |
| Config | `python-dotenv` |

---

## 📦 Dataset

**games.csv** — a curated list of video game titles used to populate the game selector.

Place the file inside the repo like this:

```
Lore-Master-OS-Gamyopedia/
└── data/
    └── games.csv
```

> The CSV must contain at least a `name` column with game titles. You can expand it with additional metadata columns as needed.

---

## 🧠 How It Works

The app builds a structured prompt from your selections and feeds it to **LLaMA 3.1 8B Instruct** via the HuggingFace Inference API.

**Prompt variables:**
- `option` — selected game title
- `style` — chosen narrator voice pack
- `depth` — word count instruction mapped from the depth slider
- `spoilers` — spoiler protection level
- `focus` — selected skill tree targets (e.g. "Main Plot ⚔️, World Building 🌍")
- `format_type` — output format (Story, Bullet Points, etc.)

**Generation loop:**

```
Prompt → LLaMA response → check if ends in sentence
  ↳ if incomplete → continue with "seamless continuation" prompt
  ↳ repeat up to 10 times → combine all chunks → display
```

This ensures full, coherent long-form outputs without truncation.

---

## 🗂️ Project Structure

```
Lore-Master-OS-Gamyopedia/
│
├── app.py              # Streamlit UI — main entry point
├── template.py         # Prompt template helper / builder
├── Template.json       # LangChain prompt template (loaded at runtime)
│
├── data/
│   └── games.csv       # Game titles dataset
│
├── .env                # API keys (not committed)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/RupStrange/Lore-Master-OS-Gamyopedia.git
cd Lore-Master-OS-Gamyopedia
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up your HuggingFace API token**

Create a `.env` file in the root directory:
```
HUGGINGFACEHUB_API_TOKEN=your_token_here
```
Get a free token at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

> **Note:** You need a HuggingFace account with access to `meta-llama/Llama-3.1-8B-Instruct`. Request access at [https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)

**5. Add your games dataset**

Place your `games.csv` inside the `data/` folder.

---

## ▶️ Usage

```bash
streamlit run app.py
```

Then:
1. Select a game from the dropdown (or type a custom title)
2. Choose your narrator voice pack and lore depth from the sidebar
3. Pick your skill tree focus areas
4. Select an output format
5. Hit **PRESS START / EXECUTE** and let the lore flow

---

## ⚠️ Known Limitations

- Dependent on HuggingFace Inference API availability — may time out under load
- LLaMA 3.1 8B can occasionally lose narrative coherence on very long "Completionist" outputs
- Game knowledge is limited to the model's training data — niche or newer titles may produce generic results
- Custom game titles (typed in manually) may yield variable quality depending on how well-known the game is

---

## 🔮 Future Improvements

- Swap HuggingFace endpoint for local Ollama inference (zero API dependency)
- Add support for exporting lore as PDF or Markdown files
- Expand `games.csv` with genre, release year, and platform metadata for smarter prompting
- Add a "Lore History" panel to revisit previously generated content
- Integrate Wikipedia/IGDB API for factual game data injection into prompts
- Support more LLMs (Mistral, Gemma, Claude via API)

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

1. Fork the repo
2. Create your branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Built with 🕹️ by <a href="https://github.com/RupStrange">RupStrange</a></p>
