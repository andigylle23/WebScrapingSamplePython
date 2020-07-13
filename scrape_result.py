# finding the description based on meta property or title
def get_description(html):
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find("meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find("meta", property="twitter:description").get('content')
    elif html.find("title"):
        description = html.find("title").contents
    return description

# finding the site name based on meta property or url 
def get_site_name(html, url):
    if html.find("meta", property="og:site_name"):
        sitename = html.find("meta", property="og:site_name").get('content')
    
    elif html.find("meta", property='twitter:title'):
        sitename = html.find("meta", property="twitter:title").get('content')
    else:
        sitename = url.split('//')[1]
        return sitename.split('/')[0].rsplit('.')[1].capitalize()
    return sitename
