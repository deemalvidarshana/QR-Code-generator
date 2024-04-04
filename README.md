# URL QR Code Generator

This is a simple Python application built with Tkinter that generates QR codes for URLs entered by the user.

## Features

- Allows users to input one or multiple URLs separated by commas.
- Generates QR codes for each URL entered.
- Provides an option to download the generated QR code image.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/deemalvidarshana/QR-Code-generator
    ```

2. Navigate to the project directory:

    ```bash
    cd url-qr-code-generator
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Enter the URL(s) you want to generate QR codes for into the input field. If entering multiple URLs, separate them with commas.
3. Click on the "Generate QR Codes" button.
4. The generated QR codes will be displayed on the screen along with a "Download" button for each QR code. Click on the "Download" button to save the QR code image to your Downloads directory.

## Dependencies

- `tkinter`: Python's standard GUI (Graphical User Interface) package.
- `qrcode`: Library for generating QR codes.
- `PIL`: Python Imaging Library for working with images.

## License

This project is licensed under the [MIT License](LICENSE).

