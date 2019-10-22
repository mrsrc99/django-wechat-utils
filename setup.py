import setuptools


# with open("README.md", "r") as fh:
# 	long_description = fh.read()

long_description = 'https://github.com/suckmybigdick/django-wechat-utils'


setuptools.setup(
	name = "django-wechat-utils",
	version="0.0.1",
	auth="awam009",
	author_email="saiawam@163.com",
	description="django-wechat-utils for wechat-app-user's login/register/auth, and message_template",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/suckmybigdick/django-wechat-utils",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	install_requires=[
		"requests==2.9.1",
		"cryptography",
		"setuptools==20.7.0",
		"Django==1.11.17",
		"itsdangerous==0.24",
		"djangorestframework==3.9.2",
	],
)
