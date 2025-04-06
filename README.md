# Aplaybox Daily Checker

This project automates the daily login and check for the Aplaybox website at [Aplaybox Model Details](https://www.aplaybox.com/details/model/xfyv7yIWHaxH).

## Features
- Logs in daily using a stored cookie.
- Checks the specified page and prints the page title.
- Runs automatically via GitHub Actions.

## Setup

### Prerequisites
- Python 3.x installed.
- A valid cookie for the Aplaybox website.

### Local Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Aplaybox_Checker
   ```
2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install undetected-chromedriver selenium
   ```
3. Set the `APLAYBOX_COOKIE` environment variable:
   ```bash
   set APLAYBOX_COOKIE=your_cookie_string
   ```
4. Run the script:
   ```bash
   python aplaybox_checker.py
   ```

### GitHub Actions Setup
1. Fork this repository.
2. Go to `Settings > Secrets and variables > Actions` in your GitHub repository.
3. Add a new secret named `APLAYBOX_COOKIE` and paste your cookie string.
4. The workflow will run daily at midnight UTC.

## Files
- `aplaybox_checker.py`: The main script for logging in and checking the page.
- `.github/workflows/daily_check.yml`: The GitHub Actions workflow for automation.

## Notes
- Ensure your cookie is valid and updated regularly.
- The script uses Selenium and undetected-chromedriver to bypass bot detection.

## License
This project is licensed under the MIT License.