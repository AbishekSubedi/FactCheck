# FactCheck

FactCheck is a web application that analyzes user-provided text for various attributes, including:

- **Fake News Detection**: Evaluates the likelihood of the text being fake news, providing confidence levels and reasons.
- **AI-Generated Content Detection**: Assesses whether the text is AI-generated, along with a confidence score.
- **Sentiment Analysis**: Determines the sentiment of the text and provides a polarity score.
- **Fact-Checking**: Offers factual verification of the content, if applicable.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User-Friendly Interface**: Interactive chat-like interface for users to input text and receive analysis.
- **Real-Time Analysis**: Immediate feedback on the input text, including fake news detection, AI-generated content detection, sentiment analysis, and fact-checking.
- **Backend Integration**: Utilizes a Flask-based backend to process and analyze the text.

## Getting Started

To deploy your own instance of FactCheck using GitHub Pages, follow these steps:

### Forking the Repository

1. **Sign in to GitHub**: Ensure you're logged into your GitHub account. If you don't have one, [sign up here](https://github.com/signup).
2. **Navigate to the FactCheck Repository**: Visit the original repository at: [https://github.com/spoud001/FactCheck](https://github.com/spoud001/FactCheck).
3. **Fork the Repository**:
   - Click the "Fork" button at the top-right corner of the repository page.
   - Choose your GitHub account as the destination for the fork. This creates a copy of the repository under your account.

### Setting Up GitHub Pages

1. **Navigate to Your Forked Repository**:
   - Go to `https://github.com/your-username/FactCheck` (replace `your-username` with your GitHub username).
2. **Access Repository Settings**:
   - Click on the "Settings" tab within your repository.
3. **Enable GitHub Pages**:
   - In the "Settings" menu, select "Pages" from the sidebar.
   - Under "Source", choose the branch to deploy (typically `main` or `gh-pages`).
   - Click "Save".
4. **Access Your Deployed Site**:
   - After a few minutes, your site will be available at: `https://your-username.github.io/FactCheck/`.

**Note:** If the original repository has a `gh-pages` branch, GitHub Pages will automatically build your fork. It may take up to 10 minutes for the site to become available. If the site doesn't appear, try making a minor commit to trigger the build process.

## Usage

Once your GitHub Pages site is live:

1. **Navigate to Your Deployed Site**: Visit `https://your-username.github.io/FactCheck/`.
2. **Interact with the Application**:
   - Enter text to analyze in the input field.
   - Click the "Submit" button.
   - View analysis results displayed in the chat box.

## Contributing

Contributions are welcome! To contribute:

1. **Fork the Repository**: Follow the [forking instructions](#forking-the-repository) above.
2. **Create a New Branch**:
   ```bash
   git checkout -b feature/YourFeatureName
3. **Commit Your Changes**:
    ```bash
    git commit -m "Add new feature"
4. **Push to Your Branch**:
    ```bash
    git push origin feature/YourFeatureName
5. **Open a Pull Request**:
    Navigate to the original repository and open a pull request with a detailed description of your changes.
