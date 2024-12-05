# CURL to Make.com HTTP Module Converter

Simple CLI tool to convert CURL commands into Make.com HTTP module configuration in JSON format.

## Features

- Convert CURL commands to Make.com HTTP module JSON configuration
- Support for multiline CURL input
- Multiple input methods (interactive, file, direct command)
- Automatic copying to clipboard
- JSON file export
- Support URL parameters and headers parsing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/curl-to-make-module.git
cd curl-to-make-module
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install pyperclip
```

## Usage

### Interactive Mode
```bash
python main.py
```
Enter your CURL command and press Enter twice to finish input.

### File Mode
Save your CURL command to a file (e.g. curl.txt):
```bash
curl --request GET \
     --url 'https://api.example.com/endpoint' \
     --header 'accept: application/json' \
     --header 'x-api-key: your-api-key'
```

Then run:
```bash
python main.py --file curl.txt
```

### Direct Mode
```bash
python main.py --curl "curl --request GET --url 'https://api.example.com/endpoint' --header 'accept: application/json'"
```

## Project Structure

- `main.py` - Main CLI application
- `curl_converter.py` - CURL to JSON converter logic
- `tools.py` - Helper functions for file operations and clipboard
- `requirements.txt` - Python dependencies

## Output

The converter produces:
1. JSON file `result.json` with Make.com HTTP module configuration
2. Copies the JSON to clipboard automatically
3. Shows operation status in console

## Error Handling

The tool includes error handling for:
- Invalid CURL commands
- File reading/writing issues
- JSON parsing errors
- Clipboard operations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
