BOT_NAME = 'notonthehighstreet'

SPIDER_MODULES = ['notonthehighstreet.spiders']
NEWSPIDER_MODULE = 'notonthehighstreet.spiders'

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 5

LOG_LEVEL = 'INFO'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'scrapy.core.scraper': {
            'level': 'ERROR',
        },
    },
}

ITEM_PIPELINES = {
    'notonthehighstreet.pipelines.NotonthehighstreetPipeline': 300,
}

DATABASE = {
    'drivername': 'sqlite',
    'database': 'products.db'
}