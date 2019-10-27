# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/home/kostia/islands/island-manager'],
             binaries=[('./lib/vendor/linux/libboost_python37.*', './lib/vendor/linux/')],
             datas=[('./os_defaults/', 'os_defaults'),  ('default_config.json', '.'), ('version', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')
