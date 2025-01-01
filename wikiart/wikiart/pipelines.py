# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WikiartPipeline:
    def process_item(self, item, spider):
        item["title"] = item["title"].strip() if item["title"] else None
        item['media'] = self.combine_list(item['media'])
        item['dimensions'] = self.extract_dimensions(item['dimensions'])
        item['location'] = item['location'] if item['location'] else None
        item['media'] = item['media'] if item['media'] else None

        return item
    
    def combine_list(self, media_list):
        return ", ".join(media_list)

    def extract_dimensions(self, data_list):
        if len(data_list) > 1:
            # Clean and return the second element
            return data_list[1].strip()
        else:
            # Handle case where second element is missing
            return ""