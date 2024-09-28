import requests

def download_wav_file(url, save_path):
    # Send a HTTP GET request to the URL
    response = requests.get(url, stream=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Open a file with the specified save path in binary write mode
        with open(save_path, 'wb') as file:
            # Write the content to the file in chunks
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"File downloaded successfully and saved as {save_path}")
    else:
        print(f"Failed to download file. HTTP Status Code: {response.status_code}")

# # Example usage
# url = 'http://pharmacy.umich.edu/sites/default/files/acebutolol.wav'
# save_path = 'your_local_file.wav'

# download_wav_file(url, save_path)
