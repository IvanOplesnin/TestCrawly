BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"

ADDONS = {}

ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "myproject.middlewares.MyprojectDownloaderMiddleware": 100,
}

ITEM_PIPELINES = {
    "myproject.pipelines.CreatePipeline": 300,
}
