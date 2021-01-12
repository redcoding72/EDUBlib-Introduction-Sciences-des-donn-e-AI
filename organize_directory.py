import os
import shutil
print('welcome in organize.py script - happy clean folder')

current_dir = os.path.dirname(os.path.realpath(__file__))

for filename in os.listdir(current_dir):
  # Organize Images into Images folder
    if filename.endswith(("png", "jpg", "gif", "jpeg", "JPG", "bmp", "tif", "tiff")):
        if not os.path.exists('Images'):
            os.mkdir('Images')
        shutil.copy(filename, 'Images')
        os.remove(filename)
        print('Done in Images')

 # Organize Videos into Videos folder
    if filename.endswith(("avi", "mp4", "mkv", "webm", "mov")):
        if not os.path.exists('Video'):
            os.mkdir('Video')
        shutil.copy(filename, 'Video')
        os.remove(filename)
        print('Done in Video')

  # Organize Docs into Documents folder
    if filename.endswith(("docx", "doc", "xml", "xmlx", "pdf", "txt", "xlsx", "rtf", "xlsx", "xls")):
        if not os.path.exists('Documents'):
            os.mkdir('Documents')
        shutil.copy(filename, 'Documents')
        os.remove(filename)
        print('Done in Documents')

  # Organize codes files into Codes folder
    if filename.endswith(("py", "css", "html", "php", "js", "bash")):
        if not os.path.exists('Codes'):
            os.mkdir('Codes')
        shutil.copy(filename, 'Codes')
        os.remove(filename)
        print('Done in Codes')

  # Organize applications files into Programs folder
    if filename.endswith(("exe", "apk", "dmg")):
        if not os.path.exists('Programs'):
            os.mkdir('Programs')
        shutil.copy(filename, 'Programs')
        os.remove(filename)
        print('Done in Programs')

  # Organize Torrents files into Torrents folder
    if filename.endswith(("torrent")):
        if not os.path.exists('Torrents'):
            os.mkdir('Torrents')
        shutil.copy(filename, 'Torrents')
        os.remove(filename)
        print('Done in Torrents')

  # Organize compressed files into Compressed folder
    if filename.endswith(("zip", "rar", "7zip")):
        if not os.path.exists('Compressed'):
            os.mkdir('Compressed')
        shutil.copy(filename, 'Compressed')
        os.remove(filename)
        print('Done in Compressed')

  # Organize Audio files into Music folder
    if filename.endswith(("mp3", "wav")):
        if not os.path.exists('Music'):
            os.mkdir('Music')
        shutil.copy(filename, 'Music')
        os.remove(filename)
        print('Done in Music')

 # Organize Adobe files into Adobe folder
    if filename.endswith(("psd", "ai", "indd")):
        if not os.path.exists('PSD'):
            os.mkdir('PSD')
        shutil.copy(filename, 'PSD')
        os.remove(filename)
        print('Done in PSD')

 # Organize PowerPoint into PowerPoint folder
    if filename.endswith(("ppt", "pptx")):
        if not os.path.exists('PowerPoint'):
            os.mkdir('PowerPoint')
        shutil.copy(filename, 'PowerPoint')
        os.remove(filename)
        print('Done in PowerPoint')

print('Done Organizing This Folder !')
