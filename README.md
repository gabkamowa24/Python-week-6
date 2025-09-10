# 🌍 Ubuntu Image Fetcher

A mindful Python tool for downloading images from the web, designed with the principles of **Ubuntu**:  
**Community, Respect, Sharing, and Practicality**.

This program allows you to fetch one or more images by simply pasting their URLs, ensures safe downloading, avoids duplicates, and organizes your images into a dedicated folder called `Fetched_Images`.

---

## ✨ Features

- ✅ Fetch one or multiple images from the web  
- ✅ Creates a `Fetched_Images` directory automatically  
- ✅ Ensures images are saved in binary mode  
- ✅ Extracts filenames from URLs (or generates safe ones if missing)  
- ✅ Prevents duplicate downloads by checking file hashes  
- ✅ Handles errors gracefully without crashing  
- ✅ Respects safety by checking HTTP headers (only saves valid images)  

---

## 🛠️ Installation & Setup

### Requirements
- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests

🚀 Usage

Run the script:

python ubuntu_fetcher.py

Example interaction:

Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (comma separated): https://example.com/ubuntu-wallpaper.jpg, https://example.com/another.png
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg
✓ Successfully fetched: another.png
✓ Image saved to Fetched_Images/another.png

Connection strengthened. Community enriched.

Your images will be saved inside the Fetched_Images directory.
🔒 Safety Precautions

    Only downloads files with valid image/* content type

    Skips duplicate images using MD5 file hash

    Times out requests after 10 seconds to avoid hanging

🌱 Ubuntu Principles in Action

    Community: Connects to the wider web to fetch and share resources

    Respect: Handles errors gracefully without crashing

    Sharing: Stores all images in a well-organized directory for later use

    Practicality: Provides a real-world tool for mindful digital collection

📂 Project Structure

Ubuntu_Requests/
│
├── ubuntu_fetcher.py   # Main script
├── README.md           # Project documentation
└── Fetched_Images/     # Folder where images are saved

🤝 Contributing

Feel free to fork this project, suggest improvements, or open issues.
Together, we strengthen connections and enrich our communities.
📜 License

This project is open-source under the MIT License.
Use, share, and improve — in the spirit of Ubuntu.


---
