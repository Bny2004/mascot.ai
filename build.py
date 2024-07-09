import PyInstaller.__main__

PyInstaller.__main__.run([
    'src/mascot_ai.py',
    '--clean',
    '--onefile',
    '--name',
    'mascot.ai',
    '--icon',
    'assets/mascot.ai.ico',
    '--version-file',
    'file_version_info.txt',
])
