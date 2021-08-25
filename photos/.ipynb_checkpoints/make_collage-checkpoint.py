from PIL import Image, ImageDraw

collage = Image.new("RGBA", (1500,1500), color=(255,255,255,255))
lst = [100, 200, 300, 400, 500, 600, 700, 800, 900]

c=0
for i in range(0,1500,500):
    for j in range(0,1500,500):
        file = "Desktop/"+str(lst[c])+".jpg"
        photo = Image.open(file).convert("RGBA")
        photo = photo.resize((500,500))        
        
        collage.paste(photo, (i,j))
        c+=1
collage.show()