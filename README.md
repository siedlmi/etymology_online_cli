Here’s a README.md file for your Etymonline CLI Tool. This document includes an introduction, installation instructions, usage examples, and contribution guidelines.

📜 Etymonline CLI Tool

A command-line tool to fetch word etymologies and related words from Etymonline.

🚀 Features:
	•	Fetches detailed etymology of a word.
	•	Retrieves related words for further exploration.
	•	Provides clickable links to Etymonline.
	•	Clean and colorful terminal output.
	•	Works directly from the command line (no need to type python before execution).

🛠 Installation

1️⃣ Clone the Repository

git clone https://github.com/yourusername/etymonline-cli.git
cd etymonline-cli

2️⃣ Install Dependencies

Ensure you have Python 3 and install the required dependencies:

pip install -r requirements.txt

3️⃣ Make the Script Executable

chmod +x etymonline_cli.py

4️⃣ (Optional) Add to PATH

To run the script from anywhere:

mv etymonline_cli.py /usr/local/bin/etymonline

Now, you can simply run:

etymonline history

instead of:

python etymonline_cli.py history

🚀 Usage

To look up a word:

etymonline word

Example:

etymonline history

Output:

┌───────────────────────────────────────────┐
│  🔗 https://www.etymonline.com/word/history │
└───────────────────────────────────────────┘

┌──────────────────────────────┐
│  Etymology of 'history'      │
└──────────────────────────────┘

late 14c., "relation of incidents" (true or false), from Old French estoire, 
estorie "story; chronicle, history" (12c., Modern French histoire), and directly 
from Latin historia "narrative of past events, account, tale, story," from Greek 
historia "a learning or knowing by inquiry; an account of one's inquiries; 
knowledge, account, historical account, record, narrative," from historein "inquire," 
from histor "wise man, judge," from PIE *wid-tor-, from root *weid- "to see" (see vision).

┌───────────────────────────────────────────┐
│  Related Words ([View More](https://www.etymonline.com/word/history/related)) │
└───────────────────────────────────────────┘
[blue]historian[/blue], [blue]historic[/blue], [blue]prehistoric[/blue]

🔧 How It Works
	•	Scrapes Etymonline using BeautifulSoup and requests.
	•	Retrieves etymology and related words.
	•	Displays results using the rich library for a better CLI experience.

🛠 Contributing

We welcome contributions! To contribute:
	1.	Fork the repository.
	2.	Clone your fork.
	3.	Create a feature branch.
	4.	Commit changes.
	5.	Push to your fork and create a Pull Request.

📜 License

This project is licensed under the MIT License.

📬 Contact

For questions or suggestions, feel free to open an issue or contact me at your.email@example.com.

Let me know if you need any modifications before uploading to GitHub! 🚀🔥