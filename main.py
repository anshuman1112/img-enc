from Tkinter import *
import tkMessageBox
from PIL import Image
from tkFileDialog import askopenfilename

def check():
   #print "Choose an image:"
   aboutstud.delete(1.0,END)
   aboutstud.insert(END, "Choose an image:")
   Tk().withdraw()
   fi = askopenfilename(filetypes=[("Png","*.png"),("Jpeg","*.jpg"),("Jpeg","*.jpeg"),("Bmp","*.bmp"),("GIF","*.gif")])
   picture = Image.open(fi).convert("RGB")
   

   if(picture.getpixel((111,291))==(4,3,5)):
      decode(picture)
   else:
      encode(picture)
   



lis= [['a',1],['b',2],['c',3],['d',4],['e',5],['f',6],['g',7],['h',8],['i',9],['j',10],['k',11],['l',12],['m',13],['n',14],['o',15],['p',16],['q',17],['r',18],['s',19],['t',20],['u',21],['v',22],['w',23],['x',24],['y',25],['z',26],['0',27],['1',28],['2',29],['3',30],['4',31],['5',32],['6',33],['7',34],['8',35],['9',36],['.',37],['!',38],[' ',39],['Null',40],['A',41],['B',42],['C',43],['D',44],['E',45],['F',46],['G',47],['H',48],['I',49],['J',50],['K',51],['L',52],['M',53],['N',54],['O',55],['P',56],['Q',57],['R',58],['S',59],['T',60],['U',61],['V',62],['W',63],['X',64],['Y',65],['Z',66],['@',67],['#',68],['$',69],['%',70],['&',71],['(',72],[')',73],['_',74],['-',75],['+',76],['=',77],[':',78],[';',79],['"',80],["'",81],['?',82],['/',83],['^',84],[',',85],['*',86],['`',87],['~',88]]

def encode(picture):
   
   
   #print "Choose a message file:"
   aboutstud.delete(1.0,END)
   aboutstud.insert(END, "Choose a message file:")
   #Tk().withdraw()
   filename = askopenfilename()
   point = filename.find('.')
   n_filename= filename[:point+1] + 'png'
   #print n_filename

   f = open(filename)   
   page = f.read()
   width, height = picture.size
   i=0
   new_color=0
   x=0
   y=0
   
   for x in range(width):
      for y in range(height):
         r,g,b = picture.getpixel( (x,y) )
         for e in lis:
            if e[0]==page[i]:
                new_color= e[1]
                break

         i=i+1
         
         if i==len(page):
            break
         picture.putpixel((x,y),(new_color,g,b))
      if i==len(page) :
         break

   picture.putpixel((x,y),(40,0,0))
   picture.putpixel((111,291),(4,3,5))   
   picture.save(n_filename,'PNG')
   tkMessageBox.showinfo("Picrypt 1.0","Encoded succesfully !! You can find your encoded image where your message file was located.")
    
   
def decode(picture):
   
   width, height = picture.size
   i=None
   s=[]
   x=0
   y=0
   current_color=0
   for x in range(width):
      for y in range(height):
         current_color,g,b = picture.getpixel( (x,y) )
         
         #print current_color,x,y
         for e in lis:
            if e[1]==current_color:
               if(e[0]!='Null'):
                  s.append(e[0])
               i=e[0]

         
         
         if i=='Null':
            break
      
         
         
         
      if i=='Null' :
         break

   a= ''.join(s)
   aboutstud.delete(1.0,END)
   aboutstud.insert(END,"Decoded message:  "+ a)
   
   
root =Tk()
root.title('Picrypt 1.0')
root.geometry('800x500+100+100')

menubar =Menu(root)
filemenu= Menu(menubar, tearoff= 0)

filemenu.add_command(label= "Encode/Decode", command= check )
filemenu.add_separator()
filemenu.add_command(label = "Quit", command  =root.destroy)
menubar.add_cascade(label = "File", menu= filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label = "About Me")
menubar.add_cascade(label = "Help",menu= helpmenu)

root.config(menu=menubar)

aboutstud=Text(root)
aboutstud.insert(END, "Welcome to Picrypt 1.0 !!")
aboutstud.pack()
#Label (text='enter the file name').pack(side=TOP,padx=10,pady=10)
#Entry(root, width=10).pack(side=TOP,padx=10,pady=10)
#Button(root, text='Encode/Decode',command  = check).pack(side= LEFT)
#Button(root, text='Encode',command = encode).pack(side= LEFT)

Button(root, text='Exit' ,command= root.destroy,width = 10).pack(side= "bottom",padx=15,pady=15)
#Button(root, text='Decode',command  =decode).pack(side= RIGHT)
root.mainloop()

