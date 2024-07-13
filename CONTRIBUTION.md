# Contribution Guidelines

Thank you for considering contributing to **promptxml**! We welcome contributions from the community and are grateful for your support.

## Setup

To get started with contributing to this project, please follow these steps:

1. **Fork the Repository**

   Fork the repository on GitHub and clone your fork locally.

   ```bash
   git clone https://github.com/your-username/promptxml.git
   cd promptxml
   ```

2. **Install Poetry**

   Ensure you have [Poetry](https://python-poetry.org/) installed. You can install it using the following command:

   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

3. **Install Dependencies**

   Install the project dependencies, including the development dependencies, by running:

   ```bash
   poetry install --with dev
   ```

4. **Install pre-commit Hooks**

   Install the pre-commit hooks to ensure code quality:

   ```bash
   pre-commit install
   ```

## Code Formatting and Linting

Before submitting a pull request, please ensure your code is formatted and linted correctly. We use `isort` for sorting imports, `black` for code formatting, and `mypy` for type checking. Run the following commands to format and check your code:

```bash
# Sort imports
isort .

# Format code
black .

# Type check
mypy .
```

## Submitting a Pull Request

Once you've made your changes, follow these steps to submit a pull request:

1. **Create a Branch**

   Create a new branch for your feature or bugfix:

   ```bash
   git checkout -b your-feature-branch
   ```

2. **Commit Your Changes**

   Commit your changes with a descriptive commit message:

   ```bash
   git add .
   git commit -m "Description of your changes"
   ```

3. **Push to Your Fork**

   Push your branch to your fork on GitHub:

   ```bash
   git push origin your-feature-branch
   ```

4. **Submit a Pull Request**

   Open a pull request on the original repository. Provide a clear description of your changes and any relevant information for the reviewers.

## Thank You!

Thank you for your contributions! We appreciate your effort and look forward to collaborating with you.