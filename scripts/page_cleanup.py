from bs4 import BeautifulSoup, Doctype
import glob

#file_path = "../book/_build/_page/Debugging/html"
file_path = "../book/_build/html/"
notebooks = glob.glob("../*.ipynb")
notebooks = [nb[3:-5] for nb in notebooks]

def cleanup(nb):
	html_doc = ""
	with open((file_path+nb), "r") as fr:
		html_doc = fr.read()
	soup = BeautifulSoup(html_doc, 'html.parser')

	# Remove <!DOCTYPE>
	for item in soup.contents:
		if isinstance(item, Doctype):
			item.extract()

	# Remove <html>
	try:
		soup.find("html").replaceWithChildren()
	except:
		pass

	# Remove <head>
	try:
		soup.head.extract()
	except:
		pass

	# Remove topbar and sidebar
	try:
		soup.find("div", {"class":"row topbar fixed-top container-xl"}).extract()
	except:
		pass

	try:
		soup.find("div", {"class":"col-12 col-md-3 bd-sidebar site-navigation show"}).extract()
	except:
		pass

	# Modify margin to center page
	# TODO Fix this with CSS instead of modifying tag attributes
	try:
		mod_attr = soup.find("div", {"class":"col-12 col-md-9 pl-md-3 pr-md-0"})
		mod_attr["style"] = "margin: auto;"
	except:
		pass

	with open((file_path+nb), "w") as fw:
		fw.write(str(soup))

for nb in notebooks:
	#print(nb)
	cleanup(nb+"html")

