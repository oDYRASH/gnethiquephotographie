import os

# Directory where the script is located
directory = os.getcwd()

# Loop through each file in the directory
for file_name in os.listdir(directory):
    # Replace 'imageName' with the actual file name in the HTML snippet
    html_snippet = f'<div class="col-lg-3 col-sm-6 col-12 shortfilms gallery-item isotope-item"><img class="img-fluid w-100" src="assets/img/gallery/traiteur/{file_name}" alt="" /></div>'
    
    # Print the modified HTML snippet
    print(html_snippet)
