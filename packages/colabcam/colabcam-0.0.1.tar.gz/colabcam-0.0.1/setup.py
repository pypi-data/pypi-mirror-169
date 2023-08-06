# coding:utf-8

from setuptools import setup
# or
# from distutils.core import setup  
foruser ='''
# Author:KuoYuan Li   
colabcam.take_photo(filename)  
cvImg = colabcam.take_img()  
'''
setup(
        name='colabcam',   
        version='0.0.1',   
        description='take picture from cam in colab',
        long_description=foruser,
        author='KuoYuan Li',  
        author_email='funny4875@gmail.com',  
        url='https://pypi.org/project/colabcam',      
        packages=['colabcam'],   
        include_package_data=True,
        keywords = ['colab', 'webcam','take_photo','take_img'],   # Keywords that define your package best
        #install_requires=['threading'],
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
      ],
)
