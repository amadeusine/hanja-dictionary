import sqlite3
import utf8csv

con = sqlite3.connect('hanjadic.sqlite')
new_hanjas = utf8csv.UnicodeReader(file('hanja-filtered.csv'))

for row in new_hanjas:
    hanja = row[6]
    hanja = hanja.replace('-','')
    found = False
    for row in con.execute('select * from hanjas where hanja = ?', (hanja,)):
        found = True
        #print row
    if not found:
        #print row[6].encode('utf-8')
        print u"INSERT INTO `hanjas` VALUES ('%s','%s',NULL,'%s',NULL);".encode('utf-8') % (
            (' '.join(x for x in row[6])).encode('utf-8'),
            row[1].encode('utf-8'),
            row[3].lower().encode('utf-8')
          )
