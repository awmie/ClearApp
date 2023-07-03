from setuptools import setup

APP = ['mainApp.py']
DATA_FILES = ['icon.gif']
OPTIONS ={
    'packages': [],
    'iconfile': 'icon.gif',
    'plist': {
        'CFBundleDevelopmentRegion': 'English',
        'CFBundleIdentifier': "com.awmie",
        'CFBundleVersion': "1.0.0",
        'NSHumanReadableCopyright': u"Copyright © 2023, awmie, All Rights Reserved"}
}

setup(
    name='Clear',
    app = APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
     
)