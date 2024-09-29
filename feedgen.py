from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from time import strftime, gmtime

class FeedGenerator:
    def __init__(self, title, link, description):
        
        self._feed = Element("rss")
        self._feed.set("version", "2.0")
        self._feed.set("xmlns:media", "http://search.yahoo.com/mrss/")

        self._channel = channel = SubElement(self._feed, "channel")
        
        title_elem = SubElement(channel, "title")
        title_elem.text = title
        
        link_elem = SubElement(channel, "link")
        link_elem.text = link
        
        description_elem = SubElement(channel, "description")
        description_elem.text = description

    def add_item(self, title, link, description, media, pubDate):
        item = SubElement(self._channel, "item")
        
        title_elem = SubElement(item, "title")
        title_elem.text = title
        
        link_elem = SubElement(item, "link")
        link_elem.text = link
        
        description_elem = SubElement(item, "description")
        description_elem.text = description

        pubDate_elem = SubElement(item, "pubDate")
        pubDate_elem.text = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(pubDate))

        SubElement(item, "media:content", {"url": media})


    def generate(self):
        rough_string = tostring(self._feed, "utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
    



