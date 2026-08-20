# Django Project Workflow

This project demonstrates professional git practices for Django development.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Development

Create feature branches for each change:

```bash
git checkout -b feature/your-feature develop
# Make changes
git push -u origin feature/your-feature
# Create pull request on GitHub
```