# 🤝 Contributing to PDF Summarizer

Thank you for your interest in contributing to the PDF Summarizer project! This document provides guidelines and information for contributors.

## 🚀 Quick Start

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/PdF_Summarizer.git
   cd PdF_Summarizer
   ```
3. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused

### Testing
- Test your changes thoroughly
- Ensure the application runs without errors
- Test with different PDF types and sizes
- Verify download functionality works

### Documentation
- Update README.md if adding new features
- Add docstrings to new functions
- Update requirements.txt if adding dependencies

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Operating System**: Windows/Linux/macOS version
2. **Python Version**: `python --version`
3. **Steps to Reproduce**: Detailed steps to recreate the issue
4. **Expected vs Actual Behavior**: What you expected vs what happened
5. **Error Messages**: Full error traceback if applicable
6. **PDF File**: Sample PDF that causes the issue (if relevant)

## ✨ Feature Requests

When requesting features, please:

1. **Describe the feature** in detail
2. **Explain the use case** and why it's needed
3. **Provide examples** of how it would work
4. **Consider implementation** complexity

## 🔧 Pull Request Process

1. **Update the README.md** with details of changes if applicable
2. **Update requirements.txt** if adding new dependencies
3. **Test your changes** thoroughly
4. **Ensure the application runs** without errors
5. **Submit a pull request** with a clear description

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement

## Testing
- [ ] Tested on Windows
- [ ] Tested on Linux
- [ ] Tested on macOS
- [ ] Tested with different PDF sizes

## Checklist
- [ ] Code follows PEP 8 style
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings generated
```

## 🏗️ Project Structure

```
PdF_Summarizer/
├── app.py              # Main application
├── config.py           # Configuration settings
├── run.py              # Startup script
├── requirements.txt    # Dependencies
├── README.md          # Project documentation
├── DEPLOYMENT.md      # Deployment guide
├── CONTRIBUTING.md    # This file
├── LICENSE            # MIT License
├── .gitignore         # Git ignore rules
└── .streamlit/        # Streamlit configuration
    └── config.toml    # App configuration
```

## 🎯 Areas for Contribution

### High Priority
- **Performance Optimization**: Improve processing speed
- **Error Handling**: Better error messages and recovery
- **Testing**: Add unit tests and integration tests
- **Documentation**: Improve guides and examples

### Medium Priority
- **UI/UX Improvements**: Better user interface
- **Export Formats**: Additional download formats
- **Model Integration**: Support for more AI models
- **Security**: Enhanced security features

### Low Priority
- **Internationalization**: Multi-language support
- **Mobile Support**: Mobile-friendly interface
- **API Development**: REST API for integration
- **Plugin System**: Extensible architecture

## 🐍 Development Environment

### Recommended Setup
- **Python**: 3.8 or higher
- **IDE**: VS Code, PyCharm, or similar
- **Version Control**: Git
- **Virtual Environment**: Always use venv

### Useful Commands
```bash
# Run the application
python run.py

# Check code style
pip install flake8
flake8 app.py

# Format code
pip install black
black app.py

# Type checking
pip install mypy
mypy app.py
```

## 📞 Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions and ideas
- **Email**: Contact maintainers directly for sensitive issues

## 🎉 Recognition

Contributors will be recognized in:
- **README.md** contributors section
- **Release notes** for significant contributions
- **GitHub contributors** page

## 📄 License

By contributing to this project, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to PDF Summarizer! 🚀** 