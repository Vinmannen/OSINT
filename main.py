from flask import Flask, render_template
import feedparser
import re
import nvdlib
import datetime

app = Flask(__name__)

@app.route('/')
def index():

    #pull data from different RSS feeds
    krebs_news = feedparser.parse("https://krebsonsecurity.com/feed/")
    krebs_entry = krebs_news.entries[0:4]

    thn_news = feedparser.parse("https://feeds.feedburner.com/TheHackersNews")  
    thn_entry = thn_news.entries[0:4]

    darkr_news = feedparser.parse("https://www.darkreading.com/rss_simple.asp")  
    darkr_entry = darkr_news.entries[0:4]

    talos_news = feedparser.parse("http://feeds.feedburner.com/Talos")  
    talos_entry = talos_news.entries[0:4]

    nakedsec_news = feedparser.parse("http://feeds.feedburner.com/NakedSecurity")  
    nakedsec_entry = nakedsec_news.entries[0:4]

    mandiant_news = feedparser.parse("https://www.mandiant.com/resources/rss.xml?type=article_blog")  
    mandiant_entry = mandiant_news.entries[0:4]

    bleeping_news = feedparser.parse("https://www.bleepingcomputer.com/feed/")  
    bleeping_entry = bleeping_news.entries[0:4]

    kaspersky_news = feedparser.parse("https://threatpost.com/feed/")  
    kaspersky_entry = kaspersky_news.entries[0:4]

    sentinelone_news = feedparser.parse("https://www.sentinelone.com/feed/")  
    sentinelone_entry = sentinelone_news.entries[0:4]

    therecord_news = feedparser.parse("https://therecord.media/feed/")  
    therecord_entry = therecord_news.entries[0:4]

    cisa_titles = []
    cisa_alerts = feedparser.parse("https://www.cisa.gov/uscert/ncas/all.xml")
    cisa_entry = cisa_alerts.entries[0:4]
    clean = re.compile('<.*?>')

    for e in range(0, len(cisa_entry)):
        title = re.sub(clean, "", cisa_entry[e].title)
        cisa_titles.append(title)

    end = datetime.datetime.now()
    start = end - datetime.timedelta(days=4)
    r = nvdlib.searchCVE(pubStartDate=start, pubEndDate=end)

    cves = {}

    for y in r:
        cve_score = y.score[1]
        cve_id = y.id
        cve_pubDate = y.publishedDate
        cve_lastmod = y.lastModifiedDate
        cve_url = y.url
        cve_info = y.cve
        if cve_score != None:
            cves.update({cve_id : [cve_score, cve_pubDate[0:10], cve_lastmod[0:10], cve_url, cve_info.description.description_data[0].value]})

    return render_template("index.html",krebs_entry = krebs_entry,
                                        thn_entry = thn_entry,
                                        darkr_entry = darkr_entry,
                                        talos_entry = talos_entry,
                                        nakedsec_entry = nakedsec_entry,
                                        mandiant_entry = mandiant_entry,
                                        bleeping_entry = bleeping_entry,
                                        kaspersky_entry = kaspersky_entry,
                                        cisa_entry = cisa_entry,
                                        cisa_titles = cisa_titles,
                                        therecord_entry = therecord_entry,
                                        sentinelone_entry = sentinelone_entry,
                                        cve_list = cves.items())

if __name__ == '__main__':
    app.run(host="0.0.0.0")
