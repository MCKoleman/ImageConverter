import easygui
from PIL import Image
from pathlib import Path

def main():
	selected_files = easygui.fileopenbox(title="Select files to convert", multiple=True)
	format = input("Select format to convert to:\n")
	if isinstance(selected_files, list):
		print("Converting", len(selected_files), "files to", format)
		for file in selected_files:
			image = Image.open(file)
			image = image.convert("RGB")
			image.save("./results/" + Path(file).stem + "." + format)
	print("Finished converting files")

if __name__ == '__main__':
    main()