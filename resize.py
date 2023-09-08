from PIL import Image
import os.path

def resize_image(input_file, output_file, scale=0.5):
    """Resize an image by scaling its dimensions."""
    
    # Open the input file in 'read' mode and load it as a PNG object
    img = Image.open(input_file)
        
    # Get original size of the image
    orig_w, orig_h = img.size
    
    # Calculate new size based on provided scale factor
    w = int(orig_w * scale)
    h = int(orig_h * scale)
    
    # Resize the loaded image using calculated values for desired width & height, then save at the given location/filename
    resized_img = img.resize((w, h))
    resized_img.save(output_file)

# Call the function passing your actual filename strings here...
if __name__ == "__main__":
    input_file = "images/previews/cao23mia.png"   # Replace this path with yours
    output_file = input_file   # Replace these paths accordingly
    resize_image(input_file, output_file, scale=0.5)  # Use different value according to need; e.g., use `scale=2` to double resolution