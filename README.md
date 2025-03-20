# Website to PDF Converter 🌐📄

A fast, reliable Python tool that converts any website or web page to PDF with high-quality formatting preservation. Perfect for archiving web content, creating offline documentation, or saving articles for later reading.

## ✨ Features

- 🎯 Convert any URL to a high-quality PDF
- 🎨 Preserves website styling and layout
- 📱 Handles modern web technologies and JavaScript
- 🚀 Fast and memory-efficient processing
- 💾 Automatic file naming based on URL

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
playwright install chromium
```

2. Convert a website to PDF:
```bash
python3 src/web_to_pdf.py https://example.com
```

The PDF will be saved in the `output` directory with a filename based on the URL.

## 💡 Advanced Usage

### Custom Output Path

Specify a custom output path using the `-o` or `--output` option:
```bash
python3 src/web_to_pdf.py https://example.com -o output/custom-name.pdf
```

### Examples

Convert a blog post:
```bash
python3 src/web_to_pdf.py https://blog.example.com/article -o output/article.pdf
```

Save documentation:
```bash
python3 src/web_to_pdf.py https://docs.example.com -o output/documentation.pdf
```

## 🛠 Technical Details

- Built with Python 3.8+
- Uses Playwright for web rendering
- WeasyPrint for PDF generation
- Handles dynamic content and JavaScript
- Automatic URL validation and error handling

## 📝 Notes

- Ensure you have Python 3.8 or higher installed
- Internet connection required for fetching web pages
- Output directory is created automatically
- URLs must include the protocol (http:// or https://)

## 🔍 Keywords

web to pdf converter, website to pdf, html to pdf converter, webpage archival tool, save website as pdf, web page converter, python pdf converter
