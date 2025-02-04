import base64

# Open image file in binary mode
with open("Screenshot (627).png", "rb") as image_file:
    # Encode the image to base64
    encoded_string = base64.b64encode(image_file.read()).decode()

# Open text file in write mode
with open("text.txt", "w") as f:
    # Option 1: Basic Markdown (No centering)
    f.write(f'![Image](data:image/png;base64,{encoded_string})\n')

    # Option 2: Using HTML for centering (may not work in VS Code Jupyter)
    # f.write(f'<img src="data:image/png;base64,{encoded_string}" style="display: block; margin-left: auto; margin-right: auto;">\n')
