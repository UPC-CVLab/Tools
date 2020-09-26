### Tools to crawling papers

---

> All files are under generalization, so it's better for you to run the scripts after you have read and understood them.

1. Modify the `PaperCrawl.py` according to the content in the paper website you want to crawl. After you have crawled the download link of all the pdf files, it is recommended to download them by using the  `IDM` or other tools that support bulk download.  
2. Use the `BatchRename.py ` to rename the `pdf` files based on the `CSV` file generated in the previous step.
3. Run `PaperFilter.py` to filter the `pdf` files according to the key word in the fileds we work on. It will copy the related files you download in the first step to the field-specific sub-directory .
