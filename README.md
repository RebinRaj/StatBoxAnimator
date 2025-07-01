# 📊 StatBoxAnimator

**StatBoxAnimator** is a general-purpose animation engine for visualizing the top N entities (such as players, companies, or products) as they rise and fall in ranking over time. The current implementation focuses on historical **ICC cricket batsman rankings**, rendered as an engaging animated video.

This version is a stable, modular release — not the latest iteration used in the YouTube video — but showcases all the core features. A more refined version may be released later.

> 📽️ **Watch it on YouTube**: [Cricket Ranking Animation – 1990 to 2000](https://youtu.be/2it1ejeMUxg?si=x3tR690H1IiP3XHM)


---

## 🗂️ Project Structure

```
StatBoxAnimator/
├── StatBoxAnimator.py				#Main file
├── background					#Background images
│   ├── my_podium_n2.png
│   └── new_background.png
├── data					#Output data folder
│   ├── images					#Player images
│   ├── player_list_check.txt		
│   └── tables					#Scrapped tables
├── data_getter					#Models for web scraping
│   ├── data_getter.py
│   ├── get_item_list.py
│   ├── image_getter.py
│   └── __init__.py
├── vidGen					#Modules for animation and visulaisation
│   ├── get_float_figure.py
│   ├── get_item_colors.py
│   ├── __init__.py
│   └── render_vid.py
├── vidResult					#Rendered video
│   └── cricket_rnk_bat_1990_2000.mp4
├── README.md
└── requirements.txt				#Python dependencies
```

---
### ⚙️ How It Works

StatBoxAnimator processes time-series ranking data to create animated visualizations with ranking tables and motion charts. The workflow consists of:

- **Data collection and wrangling**: Historical ICC batsman rankings are scraped from the [ICC archive](https://www.relianceiccrankings.com) using `requests` and `BeautifulSoup`, and saved into structured text tables.
- **Image handling**: Player images are downloaded via script (note: images may need manual correction).
- **Rendering pipeline**: The animation engine uses `Pillow` and `OpenCV` to draw each frame — including ranked tables, floating player avatars on a rating chart, and trajectory lines showing rating progression.
- **Modular design**: Code is organized into logical components for reproducibility and development
- **Media output**: A high-resolution `.mp4` file is generated, visualizing how the top N players move across time and rating scale.

This engine is general-purpose and can be adapted to animate rankings in domains like sports, business, social media, or Entertainment — wherever ranked entities evolve over time.

---

## 🔧 How to Run

1. **Clone the repo**
    ```bash
    git clone https://github.com/RebinRaj/StatBoxAnimator.git
    cd StatBoxAnimator
    ```

2. **Install dependencies**
    - check requiremnts.txt
    ```bash
    pip install beautifulsoup4 requests opencv-python Pillow
    ```

3. **Download and place player images**

    👉 Recommended: [Download the curated image ZIP here](https://drive.google.com/file/d/1HlcYAcI-KswJOxU7k7A3NU5OwtmPAm9N/view?usp=drive_link)  
       - Here is the link to [Download curated tables](https://drive.google.com/file/d/1_nq4hUSniMor5Bxx2Nvg7FSOKRfMk4Je/view?usp=drive_link)
    Extract it to:
    ```
    data/images/
    ```

4. **Run the animation generator**
    ```bash
    python StatBoxAnimator.py
    ```

---

## 📦 Notes

- This version is **modular and clean**, ideal for public release.
- The actual YouTube video was rendered with an updated version with visual and timing enhancements.
- Manual verification or replacement of images is highly encouraged for best quality.

---

## 📺 Demo Video

[![Watch on YouTube](https://img.youtube.com/vi/2it1ejeMUxg/0.jpg)](https://youtu.be/2it1ejeMUxg?si=x3tR690H1IiP3XHM)

---

## 🤝 Contributions

This is a solo passion project built around sports analytics and animation. Feel free to fork, adapt for other domains (e.g., music charts, social media rankings), or suggest improvements!

---

## 📄 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).
