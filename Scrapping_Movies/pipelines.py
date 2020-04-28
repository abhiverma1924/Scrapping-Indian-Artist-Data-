# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ScrappingMoviesPipeline:
    # Main funtion to set connection and creating table
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        #Sqlite3 databases is used for the purpose
        self.conn = sqlite3.connect('artist.db')
        self.curr = self.conn.cursor()

    def convertToBinaryData(filename):
        # Convert digital data to binary format
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData

    def create_table(self):
        # If table with the same name already exist drop it and create again, as the process is going to repeat again and again it is neccesary.
        self.curr.execute("""DROP TABLE IF EXISTS artist""")
        self.curr.execute("""create table artist(
                                    name TEXT,
                                    info TEXT,
                                    movie TEXT,
                                    image TEXT)""")

    def process_item(self, item, spider):
        #print("Pipeline :" + item['actor_name'][0])
        self.store_db(item)
        return item

    def store_db(self,item):
        #Data scrapped from the website is stored in the container and through a pipeline imported to database.
        self.curr.execute("""insert into artist values (?,?,?,?) """,(
            item['actor_name'][0],
            item['actor_info'][0],
            item['actor_movie'][0],
            item['actor_imageLink'][0]
        ))
        self.conn.commit()