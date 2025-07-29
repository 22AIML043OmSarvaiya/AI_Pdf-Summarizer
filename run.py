#!/usr/bin/env python3
"""
Secure PDF Summarizer - Startup Script
This script provides a simple way to launch the Streamlit application.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        import PyPDF2
        import transformers
        import torch
        import cryptography
        print("✅ All dependencies are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please run: pip install -r requirements.txt")
        return False

def main():
    print("🔒 Secure PDF Summarizer")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("app.py").exists():
        print("❌ Error: app.py not found in current directory")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("\n🚀 Starting the application...")
    print("📱 The web interface will open in your browser")
    print("🔗 URL: http://localhost:8501")
    print("\n💡 Tips:")
    print("   - First run may take 2-5 minutes to download the AI model")
    print("   - Use GPU if available for faster processing")
    print("   - AI automatically optimizes summary length")
    print("   - Press Ctrl+C to stop the application")
    print("\n" + "=" * 40)
    
    try:
        # Run the Streamlit application
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error running application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 