from scrapy.loader import ItemLoader
from scrapy.loader import processors
from .items import AuthorItem


class QuotesLoader(ItemLoader):
    """"""
    default_input_processor = processors.Compose(
        # processors.TakeFirst(),
        str.upper
        # lambda v: v.stip()
    )


class AuthorLoader(ItemLoader):
    default_item_class = AuthorItem
    default_input_processor = processors.Compose(
        processors.TakeFirst(),
        # str.upper,
        lambda values: values.strip(),
    )
    default_output_processor = processors.TakeFirst()





