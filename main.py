import fetchdata
import plot


COMPANY_NAME='apple'
URL_POOL=['https://jobs.apple.com/en-us/search?sort=relevance&location=united-states-USA']
LIMIT = 200

def main():
    keyword_dict = {'innovation': 0, 'leadership': 0, 'communication':0, 'enthusiasm':0,'passionate':0,'diversity':0,'customer':0,'team':0,'teamword':0,
    'learn':0,'flexibility':0,'impact':0,'integrity':0,'respect':0,'excellence':0,'trust':0,'accountability':0,'quality':0,'commitment':0,'people':0,
    'commitment':0,'integrity':0,'technology':0,'client':0,'best':0,'respect':0,'network':0,'performance':0,'involved':0,'exceptional':0,'empathy':0,
    'responsibility':0,'human':0,'sustainable':0,'opportunities':0,'give':0,'collaboration':0,'fast':0,'open':0,'value':0,'engage':0,'inspire':0,
    'ethical':0,'honest':0,'courage':0,'team':0,'improvement':0,'service':0,'fun':0,'willpower':0,'humble':0,'success':0,'ownership':0,'trust':0,
    'transparency':0,'fun':0,'optimize':0,'dignity':0,'results':0,'change':0,'users':0,'simplify':0,'growth':0,'family':0,}

    crawler = fetchdata.Crawler(COMPANY_NAME, URL_POOL, LIMIT, keyword_dict)
    crawler.crawl()
    print(keyword_dict)

    plotter = plot.Plotter()
    plotter.plotWordCloud(keyword_dict)

if __name__ == "__main__":
    main()