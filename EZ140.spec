# -*- mode: python -*-

block_cipher = None


a = Analysis(['EZ140.py'],
             pathex=['C:\\Users\\dylan\\Desktop\\ez140py'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='EZ140',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='C:\\Users\\dylan\\Desktop\\ez140py\\icon.ico')
