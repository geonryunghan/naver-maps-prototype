# NAVER Maps Prototype

This repository contains a simple prototype demonstrating how to interact with the NAVER Maps API using Python. It includes sample code for handling API credentials and making a basic endpoint call to retrieve geocoding information.

## Prerequisites

- Python 3.7+
- A NAVER Cloud Platform account with Maps API enabled
- NAVER Maps API credentials (Client ID and Client Secret)

## Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/geonryunghan/naver-maps-prototype.git
   cd naver-maps-prototype
   ```

2. (Optional) Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:  
   This project uses the `requests` library for HTTP calls. You can install it directly:
   ```bash
   pip install requests
   ```
   If you prefer using a `requirements.txt`, create one containing `requests==2.31.0` (or the latest version) and run:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your NAVER Maps API credentials as environment variables before running the script:  
   On Unix/macOS:
   ```bash
   export NAVER_CLIENT_ID=your_client_id
   export NAVER_CLIENT_SECRET=your_client_secret
   ```
   On Windows Command Prompt:
   ```cmd
   set NAVER_CLIENT_ID=your_client_id
   set NAVER_CLIENT_SECRET=your_client_secret
   ```

## Quick Start

After installing the dependencies and configuring your API credentials, run the sample script to make a geocode request:

```bash
python naver_maps_example.py
```

The script queries the coordinates for a default address ("Seoul City Hall") and prints the JSON response. To test other addresses, edit the `address` variable in `naver_maps_example.py`.

## Next Steps

- Explore additional NAVER Maps API endpoints, such as reverse geocoding, directions, or place search.  
- Wrap API calls into reusable functions or classes for better structure.  
- Implement error handling and respect rate limits according to the API documentation.

## License

This project is provided as a simple example and is licensed under the MIT License.
