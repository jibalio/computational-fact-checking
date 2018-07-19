from wikipedia_ia import Page, Path

page1 = Page(title="Barack Obama")
page2 = Page(title="Muslim")
#print (page1.title)
path = Path(page1, page2)
#print(path.nodes)
print(path.degrees)
print("Truth value:" + str(path.get_truthvalue()))


#print(len(page1.links))
#print (page2.title)
