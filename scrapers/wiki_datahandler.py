

import sqlite3
from .logger import log


class DataHandler:
    
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
    
    def insert_page(self,wikipage):
        # Create parameterized query
        q = "INSERT INTO `Page`(`title`,`content`,`backlinks`) VALUES (?,?,?);"
        params = (wikipage.title, wikipage.pagecontent, wikipage.backlinkcount)

        try:
        # run query
            c = self.conn.cursor()
            c.execute(q, params)
            self.conn.commit()
            c.close()
        except:
            pass

    def update(self, wikipage):
        q = "UPDATE `Page` SET `content`=? WHERE title = ?;"
        params =  (wikipage.pagecontent, wikipage.title)
        try:
        # run query
            c = self.conn.cursor()
            c.execute(q, params)
            self.conn.commit()
            c.close()
        except:
            pass

    def get_page(self, title):
        c = self.conn.cursor()
        q = "select title,content,backlinks from page where title=? collate nocase"
        c.execute(q, [title])
        all_rows = c.fetchall()
        return all_rows
        

    def get_path(self, source, dest):
        c = self.conn.cursor()
        q = "select source, dest, pathstring, cosine_similarity from `Path` where source = ? and dest = ? collate nocase"
        c.execute(q, [source, dest])
        all_rows = c.fetchall()
        return all_rows



    def insert_path(self, path):
        q = "INSERT INTO `Path`(`source`,`dest`,`pathstring`,`cosine_similarity`) VALUES (?,?,?,?);"
        params = [
            path.source, 
            path.dest, 
            path.pathstring,
            path.cosine_similarity, 
        ]
    
            
        c = self.conn.cursor()
        c.execute(q, params)
        self.conn.commit()
        c.close()


    def get_mid_title(self, mid):
        c = self.conn.cursor()
        q = "select title from `Mid` where mid = ?"
        c.execute(q, [mid])
        all_rows = c.fetchall()
        return all_rows[0][0]

    def add_mid(self, mid, title):
        q = "INSERT INTO `Mid`(`mid`,`title`) VALUES (?,?);"
        params = [
            mid, title 
        ]
        c = self.conn.cursor()
        c.execute(q, params)
        self.conn.commit()
        c.close()
       

        

