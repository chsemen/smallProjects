from PIL import Image

catIm = Image.open('zophie.png')
width, height = catIm.size
quartersizedIm = catIm.resize((int(width/2), int(height/2)))
quartersizedIm.save('quartersized.jpg')
svelteIm = catIm.resize((width, height + 300))
svelteIm.save('svelte.jpg')
