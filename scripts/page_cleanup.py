from bs4 import BeautifulSoup, Doctype
import json
import glob

#file_path = "../book/_build/_page/Debugging/html"
file_path = "book/_build/html/"
notebooks = glob.glob("*.ipynb")
notebooks = [nb[:-6] for nb in notebooks]


php_toc = {}
sec_entries = {} # ToC for each chapter

def clean_body(nb, chap):
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

	# Isolate ToC and sections
	# Remove <head>
	try:
		# Chapter ToC
		toc = soup.find(id="bd-docs-nav")
		toc_links = toc.find_all("a", class_=["reference", "internal"])
		for l in toc_links:
			title = l.contents[0].strip()
			#url = l["href"]
			if l["href"] == "#":
				php_toc[chap]["Title"] = title
				php_toc[chap]["URL"] = (chap+".html")
			#if "Title" not in php_toc[chap]:

		# Section ToC per chapter
		sec = soup.find(id="bd-toc-nav")
		sec_links = sec.find_all("a", class_=["reference", "internal", "nav-link"])
		for l in sec_links:
			key = l.contents[0].strip()
			if key not in sec_entries[chap]:
				sec_entries[chap][key] = l["href"]

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

	#with open((file_path+nb), "w") as fw:
	#	fw.write(str(soup))

for nb in notebooks:
	#print(nb)
	#if nb not in sec_entries:
	#	sec_entries[nb] = {}
	if nb not in php_toc:
		php_toc[nb] = {}
	clean_body(nb+".html", nb)

#with open("./toc.json", "w+") as toc_json:
#	json.dump(toc_entries, toc_json)
#
#with open("./sec.json", "w+") as sec_json:
#	json.dump(sec_entries, sec_json, indent=4)

#print(php_toc)

with open("./toc.php", "w+") as php_file:
	php_file.write("<?php\n$gentoc = json_decode(")
	json.dump(php_toc, php_file)
	php_file.write(");\n?>")