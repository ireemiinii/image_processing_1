import Image
#f = "C:\\Users\\Ýrem\\Desktop\\image homework\\white.jpg"   #for change
f = "C:\\Users\\Ýrem\\Desktop\\image homework\\urban3.jpg" #for decsize,sharp,threshold
img = Image.open(f)

class filtered:
    def __init__(self):
        self.size = img.size
        self.width = img.size[0]
        self.height = img.size[1]
        self.pixels = img.load()
    def dec_size(self,scale):
        self.scale = scale
        self.size=[self.size[0]/self.scale,self.size[1]/self.scale]
        img.thumbnail(self.size)
        img.save("resized.tiff", "TIFF", optimize=True)
    
    def sharp_filter(self):
        self.sharp = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,25,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        self.new_value = 0
        for a in range(self.width):
            for b in range(self.height):
                if a in (0,self.width-1) or b in (0,self.height-1):
                    self.pixels[a,b]=0
           
                else:
                    counter=0
                    self.new_value = 0
                    for i in range(5):
                        for j in range(5):
                          self.new_value =self.new_value+self.pixels[a,b]*self.sharp[counter]
                          counter+=1
                          
                    self.new_value=int(self.new_value/25)
                    if self.new_value<0:
                        self.pixels[a,b] = 0
                        
                    elif self.new_value>255:
                        self.pixels[a,b] = 255

                    else:
                        self.pixels[a,b] = self.new_value
                    
                    
       
        img.save("sharp_filtered.jpg","JPEG" ,optimize=True)     
    
    def threshold(self,value):
        self.value = value
        for i in range(self.width):
            for j in range(self.height):
                if  self.value > self.pixels[i,j]:
                    self.pixels[i,j] = 0

                elif self.value <= self.pixels[i,j]:
                    self.pixels[i,j] = 255
        img.save("threshholded.jpg", "JPEG" ,optimize=True)

    def change(self): 
        self.imageWidth=img.size[0]
        self.imageHeight=img.size[1]
        self.n=1
        for i in range(10,self.imageWidth,50):
            for j in range(10,self.imageHeight,50):
                self.pixels[i,j]=0
                self.pixels[i,j-self.n]=0
                self.pixels[i-self.n,j]=0
                self.pixels[i,j+self.n]=0
                self.pixels[i+self.n,j]=0
                
        img.save("changed.jpg", "JPEG" ,optimize=True)
                
      
                
s=filtered()
s.dec_size(4)
#s.sharp_filter()
#s.threshold(5)
#s.change()
