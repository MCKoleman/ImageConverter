import easygui
from PIL import Image
from pathlib import Path

def main():
	selected_files = easygui.fileopenbox(title="Select files to crop", multiple=True)
	left = int(input("Enter left coordinate:\n"))
	top = int(input("Enter top coordinate:\n"))
	right = int(input("Enter right coordinate:\n"))
	bottom = int(input("Enter bottom coordinate:\n"))
	if isinstance(selected_files, list):
		print(f"Cropping {len(selected_files)} files to [{left}, {top}, {right}, {bottom}]")
		for file in selected_files:
			image = Image.open(file)
			image = image.crop((left, top, right, bottom))
			image.save("./results/crop/" + Path(file).name)
	print("Finished cropping files")

if __name__ == '__main__':
    main()