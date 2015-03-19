from os import listdir
from os.path import isfile, join
import webbrowser

def filenames(mypath):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    return onlyfiles

Title="Photos"   
f=open('index.html','w+')

initial_html="""<!DOCTYPE HTML>
<html>
<head>
<link type="text/css" rel="stylesheet" href="styles.css"/>
 <script type="text/javascript" src="script.js"></script>
<meta charset="utf-8">
</head>
<body>
<h1>"""+Title+"""
</h1>
<div id="slideshow-container">
<figure id="slideshow">

"""

f.write(initial_html)
mypath="images"
files=filenames(mypath)

for i in files:
    inp="""<img src='"""+mypath+'/'+i+"""' alt='"""+i+"""' id='"""+i+"""'>"""
    print inp
    f.writelines(inp+'\n')

closing_html="""
</figure>
</div>
</body>
<footer>All Photos are owned by the creator and any reuse without permission is liable to prosecution.</footer>
</html>
"""
f.write(closing_html)
f.close()

f1=open('styles.css','w')
style="""
@keyframes fadey {
0% { opacity: 0; }
15% { opacity: 1; }
85% { opacity: 1; }
100% { opacity: 0; }
}
figure#slideshow { width: 80%; margin: 0 auto; position: relative; }
figure#slideshow img {
position: absolute; left: 0; top: 0;
width: 100%; height: auto; opacity: 0;
}
figure#slideshow img:first-child { position: relative; }
"""
f1.write(style)
f1.close()

f2=open('script.js','w')
scripts="""
window.onload = function() {
imgs = document.getElementById('slideshow').children;
interval = 8000;
currentPic = 0;
imgs[currentPic].style.webkitAnimation = 'fadey '+interval+'ms';
imgs[currentPic].style.animation = 'fadey '+interval+'ms';
var infiniteLoop = setInterval(function(){
imgs[currentPic].removeAttribute('style');
if ( currentPic == imgs.length - 1) { currentPic = 0; } else { currentPic++; }
imgs[currentPic].style.webkitAnimation = 'fadey '+interval+'ms';
imgs[currentPic].style.animation = 'fadey '+interval+'ms';
}, interval);
}
  """
f2.write(scripts)
f2.close()

webbrowser.open("index.html", new=2, autoraise=True)
    
