### 🔗 URL Shortener CLI (Linux)
A lightweight and fast command-line tool for shortening URLs using the CleanURI API. Designed specifically for Linux systems.

### 📦 Features
Shorten any long URL directly from your terminal

Minimal dependencies

Fast and easy to use

Supports both input from arguments and interactive mode

### 🛠️ Prerequisites
Linux OS

Python 3.x

requests library (pip install requests)
### 🚀 Installation

```bash
git clone https://github.com/subhamsinhadev/Short-Url-CLI.git
cd Short-Url-CLI
chmod +x shorturl.py 
```

### 🧪 Usage

```bash
./shorturl.py "https://example.com/some/very/long/url"
```

### 💡 Example Output

```bash
Original URL: https://example.com/some/very/long/url
Shortened URL: https://cleanuri.com/xyz123
```


### 📚 API Reference
This CLI uses:

POST https://cleanuri.com/api/v1/shorten

Data: url (string)

Returns: JSON { "result_url": "https://cleanuri.com/xyz123" }

### 🧑‍💻 Author

**Subham Kumar Sinha**  
📧 [LinkedIn](https://www.linkedin.com/in/subhamsinhadev)  
