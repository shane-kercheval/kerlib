data = None
with open ("full-stackstrategyconsulting.wordpress.2015-12-07.xml", "r") as myfile:
    data=myfile.read()

data = data.replace("wp:", "")
data = data.replace("content:encoded", "content")

#print(data)

import xml.etree.ElementTree
#root = xml.etree.ElementTree.parse('full-stackstrategyconsulting.wordpress.2015-12-07.xml').getroot()
root = xml.etree.ElementTree.fromstring(data)


# ---
# layout: post
# title:  "How to Form Hypotheses"
# date:   2015-10-13 11:54:34 -0800
# categories: hypotheses decisions
# excerpt: All types of decisions have implicit assumptions and hypotheses behind them.
# ---
front_matter = """---
layout: post
title:  "{0}"
date:   {1}
categories: <fill in>
excerpt: <fill in>
---"""

month_dictionary = {
'jan': '01',
'feb': '02',
'mar': '03',
'apr': '04',
'may': '05',
'jun': '06',
'jul': '07',
'aug': '08',
'sep': '09',
'oct': '10',
'nov': '11',
'dec': '12'
}


for child in root.iter('item'):
    title = child.find('title').text
    name = child.find('post_name').text
    date = child.find('pubDate').text
    content = child.find('content').text
    #Sat, 31 Aug 2013 02:16:20 +0000
    date_split = date.split()
    day = date_split[1]
    month = month_dictionary[date_split[2].lower()]
    year = date_split[3]
    time = date_split[4]
    time_long = time+date_split[5]
#    print(time_long)
    #print("   "+title)
    #print("   "+date)
    #print("   "+name)

    #YEAR-MONTH-DAY-title.md
    filename = "{}-{}-{}-{}.md".format(year, month, day, name)
    print(filename)

    # date:   2015-10-13 11:54:34 -0800
    front_matter_date = "{}-{}-{} {}".format(year, month, day, time_long)
#    print(front_matter_date)
    with open (filename, "a") as mdfile:
        mdfile.write(front_matter.format(title, front_matter_date)+"\n"+content)
