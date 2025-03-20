#!/usr/bin/env python3
"""
URL to PDF Converter
Fetches a webpage and converts it to PDF format.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright
import weasyprint
from slugify import slugify

def validate_url(url: str) -> bool:
    """Validate if the given string is a valid URL."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_output_path(url: str, output_dir: str) -> Path:
    """Generate an output path based on the URL."""
    # Create a filename from the URL
    parsed_url = urlparse(url)
    base_name = slugify(parsed_url.netloc + parsed_url.path)
    if not base_name:
        base_name = "output"
    
    # Ensure it ends with .pdf
    if not base_name.endswith('.pdf'):
        base_name += '.pdf'
    
    return Path(output_dir) / base_name

def url_to_pdf(url: str, output_path: Optional[Path] = None) -> Path:
    """
    Convert a URL to PDF.
    
    Args:
        url: The URL to convert
        output_path: Optional custom output path
    
    Returns:
        Path to the generated PDF file
    
    Raises:
        ValueError: If URL is invalid
        RuntimeError: If conversion fails
    """
    if not validate_url(url):
        raise ValueError(f"Invalid URL: {url}")
    
    # Set default output path if none provided
    if output_path is None:
        output_path = get_output_path(url, 'output')
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Use Playwright to render the page
        with sync_playwright() as p:
            # Launch browser
            browser = p.chromium.launch()
            page = browser.new_page()
            
            # Go to URL and wait for network idle
            page.goto(url, wait_until='networkidle')
            
            # Get the page content
            html_content = page.content()
            
            # Close browser
            browser.close()
        
        # Convert to PDF using WeasyPrint
        weasyprint.HTML(string=html_content).write_pdf(output_path)
        
        return output_path
    
    except Exception as e:
        raise RuntimeError(f"Failed to convert {url} to PDF: {str(e)}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Convert a URL to PDF')
    parser.add_argument('url', help='The URL to convert')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    args = parser.parse_args()
    
    try:
        output_path = Path(args.output) if args.output else None
        result_path = url_to_pdf(args.url, output_path)
        print(f"Successfully created PDF: {result_path}")
        sys.exit(0)
    
    except (ValueError, RuntimeError) as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
