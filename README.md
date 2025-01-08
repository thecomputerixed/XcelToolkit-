# XcelToolkit

XcelToolkit is a Python-powered utility designed to simplify and streamline Excel file management. Whether you need to sort files by language, organize data dynamically, or perform advanced operations, XcelToolkit provides flexible solutions for working with Excel files efficiently.

## Features

- **Dynamic Language Sorting**: Automatically detects language abbreviations (e.g., `EN`, `ES`, `AR`) in filenames and organizes files into corresponding folders.
- **Customizable**: Easily adjust sorting rules or extend the functionality to meet specific needs.
- **Automation**: Save time by automating repetitive file management tasks.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/XcelToolkit.git
   ```

2. Navigate to the project directory:
   ```bash
   cd XcelToolkit
   ```

3. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Example: Sorting Excel Files by Language

1. Place your Excel files in a folder.
2. Update the `folder_path` in the script to point to your directory.
3. Run the script:
   ```bash
   python sort_files.py
   ```
4. Files will be automatically sorted into folders based on the detected language abbreviations in their filenames.

### Supported Abbreviations

The script dynamically detects two-letter language codes (e.g., `EN`, `ES`, `AR`, etc.). No manual configuration is required.

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature description"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or suggestions, please reach out via [GitHub Issues](https://github.com/your-username/XcelToolkit/issues).

