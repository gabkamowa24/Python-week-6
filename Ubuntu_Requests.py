import requests
import os
import hashlib
from urllib.parse import urlparse

def get_filename_from_url(url, response):
    """
    Extract filename from URL or generate a safe one.
    If no filename in URL, try from Content-Type header.
    """
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # If no filename in URL, fallback to header or hash
    if not filename:
        content_type = response.headers.get("Content-Type", "")
        if "image/" in content_type:
            ext = content_type.split("/")[-1]
            filename = f"downloaded_image.{ext}"
        else:
            filename = f"downloaded_image_{hashlib.md5(url.encode()).hexdigest()[:8]}.jpg"

    return filename


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs (comma-separated)
    urls = input("Please enter one or more image URLs (comma separated): ").split(",")

    # Create directory if it doesn't exist
    os.makedirs("Fetched_Images", exist_ok=True)

    # Keep a set of downloaded hashes to prevent duplicates
    downloaded_hashes = set()

    for url in [u.strip() for u in urls if u.strip()]:
        try:
            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Check content type (only allow images)
            if "image" not in response.headers.get("Content-Type", ""):
                print(f"✗ Skipped (not an image): {url}")
                continue

            # Generate filename
            filename = get_filename_from_url(url, response)
            filepath = os.path.join("Fetched_Images", filename)

            # Check for duplicates using hash
            file_content = response.content
            file_hash = hashlib.md5(file_content).hexdigest()

            if file_hash in downloaded_hashes:
                print(f"⚠ Skipped duplicate: {filename}")
                continue

            # Save image in binary mode
            with open(filepath, "wb") as f:
                f.write(file_content)

            downloaded_hashes.add(file_hash)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error while fetching {url}: {e}")
        except Exception as e:
            print(f"✗ An error occurred with {url}: {e}")

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()
