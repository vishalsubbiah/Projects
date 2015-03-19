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
<div>
"""

f.write(initial_html)
mypath="images"
files=filenames(mypath)

for i in files:
    inp="""<button onclick="goFullscreen('"""+i+"""'); return false"><img src='"""+mypath+'/'+i+"""' alt='"""+i+"""' id='"""+i+"""'></button>"""
    print inp
    f.writelines(inp+'\n')

closing_html="""
</div>
</body>
<footer>All Photos are owned by the creator and any reuse without permission is liable to prosecution.</footer>
</html>
"""
f.write(closing_html)
f.close()

f1=open('styles.css','w')
style="""
button{
	height: 15%;
	width: 15%;
}
img{
	height: 100%;
	width: 100%;
}
"""
f1.write(style)
f1.close()

f2=open('script.js','w')
scripts="""
function goFullscreen(id) {
    // Get the element that we want to take into fullscreen mode
    var element = document.getElementById(id);
    
    // These function will not exist in the browsers that don't support fullscreen mode yet, 
    // so we'll have to check to see if they're available before calling them.
    
    if (element.mozRequestFullScreen) {
      // This is how to go into fullscren mode in Firefox
      // Note the "moz" prefix, which is short for Mozilla.
      element.mozRequestFullScreen();
    } else if (element.webkitRequestFullScreen) {
      // This is how to go into fullscreen mode in Chrome and Safari
      // Both of those browsers are based on the Webkit project, hence the same prefix.
      element.webkitRequestFullScreen();
   }
   // Hooray, now we're in fullscreen mode!
  }
  """
f2.write(scripts)
f2.close()

webbrowser.open("index.html", new=2, autoraise=True)
    
