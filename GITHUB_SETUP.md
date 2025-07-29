# 🚀 GitHub Setup Guide

This guide will help you push your PDF Summarizer project to GitHub.

## 📋 Prerequisites

1. **GitHub Account**: Create one at [github.com](https://github.com)
2. **Git Installed**: Download from [git-scm.com](https://git-scm.com)
3. **GitHub CLI** (Optional): For easier GitHub integration

## 🔧 Step-by-Step Setup

### 1. Initialize Git Repository

```bash
# Navigate to your project directory
cd PdF_Summarizer

# Initialize git repository
git init

# Add all files to git
git add .

# Make initial commit
git commit -m "Initial commit: PDF Summarizer with AI-powered summarization"
```

### 2. Create GitHub Repository

#### Option A: Using GitHub Website
1. Go to [github.com](https://github.com)
2. Click the **"+"** icon → **"New repository"**
3. Repository name: `PdF_Summarizer`
4. Description: `AI-powered PDF summarization with privacy-first design`
5. Make it **Public** or **Private** (your choice)
6. **Don't** initialize with README (we already have one)
7. Click **"Create repository"**

#### Option B: Using GitHub CLI
```bash
# Install GitHub CLI first, then:
gh repo create PdF_Summarizer --public --description "AI-powered PDF summarization with privacy-first design"
```

### 3. Connect and Push to GitHub

```bash
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/PdF_Summarizer.git

# Set main as default branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### 4. Verify Setup

1. Go to your GitHub repository URL
2. Check that all files are uploaded
3. Verify the README.md displays correctly

## 📁 Repository Structure

Your GitHub repository should contain:

```
PdF_Summarizer/
├── 📄 app.py              # Main application
├── 📄 config.py           # Configuration settings
├── 📄 run.py              # Startup script
├── 📄 requirements.txt    # Dependencies
├── 📄 README.md          # Project documentation
├── 📄 DEPLOYMENT.md      # Deployment guide
├── 📄 CONTRIBUTING.md    # Contributing guidelines
├── 📄 LICENSE            # MIT License
├── 📄 .gitignore         # Git ignore rules
├── 📄 GITHUB_SETUP.md    # This file
├── 📁 .github/           # GitHub Actions
│   └── 📁 workflows/
│       └── 📄 ci.yml     # CI/CD pipeline
└── 📁 .streamlit/        # Streamlit configuration
    └── 📄 config.toml    # App configuration
```

## 🏷️ Repository Settings

### 1. Enable GitHub Actions
1. Go to your repository → **Settings** → **Actions** → **General**
2. Select **"Allow all actions and reusable workflows"**
3. Click **"Save"**

### 2. Set Up Branch Protection (Optional)
1. Go to **Settings** → **Branches**
2. Click **"Add rule"**
3. Branch name pattern: `main`
4. Check **"Require a pull request before merging"**
5. Check **"Require status checks to pass before merging"**
6. Click **"Create"**

### 3. Add Repository Topics
1. Go to your repository main page
2. Click the gear icon next to **"About"**
3. Add topics: `pdf`, `summarization`, `ai`, `streamlit`, `python`, `nlp`

## 📊 GitHub Features Setup

### 1. Issues Template
Create `.github/ISSUE_TEMPLATE/bug_report.md`:
```markdown
---
name: Bug report
about: Create a report to help us improve
title: ''
labels: bug
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10]
 - Python Version: [e.g. 3.9]
 - Browser: [e.g. Chrome]

**Additional context**
Add any other context about the problem here.
```

### 2. Pull Request Template
Create `.github/pull_request_template.md`:
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

## 🔄 Regular Updates

### Daily Development Workflow
```bash
# Make changes to your code
# Then:

# Check status
git status

# Add changes
git add .

# Commit changes
git commit -m "Description of changes"

# Push to GitHub
git push origin main
```

### Creating Releases
1. Go to **Releases** → **"Create a new release"**
2. Tag version: `v1.0.0`
3. Release title: `PDF Summarizer v1.0.0`
4. Description: Add release notes
5. Click **"Publish release"**

## 🎯 Next Steps

### 1. Add Badges to README
Add these badges to your README.md:
```markdown
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)
```

### 2. Enable GitHub Pages (Optional)
1. Go to **Settings** → **Pages**
2. Source: **"Deploy from a branch"**
3. Branch: `main` → `/docs`
4. Click **"Save"**

### 3. Set Up Discussions
1. Go to **Settings** → **Features**
2. Enable **"Discussions"**
3. Create categories for questions and ideas

## 🚨 Troubleshooting

### Common Issues

**"Repository not found"**
- Check your GitHub username is correct
- Verify the repository exists on GitHub

**"Permission denied"**
- Use HTTPS instead of SSH
- Or set up SSH keys for GitHub

**"Large file" error**
- Check `.gitignore` excludes large files
- Use Git LFS for large files if needed

**GitHub Actions not running**
- Check Actions tab in repository
- Verify workflow file is in `.github/workflows/`

## 📞 Support

If you encounter issues:
1. Check GitHub documentation
2. Search existing issues
3. Create a new issue with details
4. Contact maintainers

---

**Your PDF Summarizer is now ready on GitHub! 🎉** 