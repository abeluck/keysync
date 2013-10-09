# -*- mode: python -*-
a = Analysis(['keysync-gui'],
             pathex=['c:\\Users\\abel\\Documents\\keysync'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
icon_dir = Tree('icons', prefix='icons')
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='KeySync.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               icon_dir,
               strip=None,
               upx=True,
               name='KeySync')
