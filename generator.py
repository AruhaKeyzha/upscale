import os
import glob
import requests
 
def upscale_image(input_image_path, output_image_path, engine_id, api_key, api_host="https://api.stability.ai", width=None, height=None):
    # Open the input image file
    with open(input_image_path, "rb") as file:
        image_data = file.read()
 
    # Set up request headers and parameters
    headers = {
        "Accept": "image/png",
        "Authorization": f"Bearer {api_key}",
    }
 
    files = {
        "image": image_data,
    }
 
    data = {}
    if width:
        data["width"] = width
    if height:
        data["height"] = height
 
    # Send POST request to the API
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/image-to-image/upscale",
        headers=headers,
        files=files,
        data=data
    )
 
    # Check the response status code
    if response.status_code != 200:
        raise Exception(f"Non-200 response: {response.text}")
 
    # Write the response content (upscaled image data) to output file
    with open(output_image_path, "wb") as f:
        f.write(response.content)
 
    print(f"Upscaled image is saved at: {output_image_path}")
 
 
# Find all PNG files in the current directory
image_files = glob.glob('*.png')
 
# Upscale each image file
for image_file in image_files:
    output_file = f"upscaled_{image_file}"
    upscale_image(image_file, output_file, "esrgan-v1-x2plus", "YOUR_API_KEY", width=1024)
 
