1.创建虚拟环境：pip install virtualenv
	 cd 创建虚拟环境的目录
	virtualenv ven_scrapy　　创建名为ven_的虚拟环境
2.进入虚拟环境：cd ven_scrapy
		cd Script
		activate
3.创建项目cmd：scrapy startproject scrapyDemo
4.添加到git仓库：cd scrapyDemow
	git init
	git remote add origin https://github.com/Guo-l-t/ScrapyDemo.git
	git push -u origin master
5. No module named 'win32api'
	pip install pypiwin32
6.运行：scrapy crawl quotes
