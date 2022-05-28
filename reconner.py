import os

def start():
	domain_to_scan = input("Enter website for scanning: ")
	if domain_to_scan:
		print(f"Scanning {domain_to_scan} with Sublist3r...")
		sublister(domain_to_scan)
		nmapper()
		glue()
	else:
		print("Wrong website. Try again.")

def sublister(link):
	os.system(f"python3 Sublist3r/sublist3r.py -d {link} -o subdomains.txt")

def nmapper():
	os.system("./auto_scan.sh")

def glue():
	os.system("python3 reports_glue.py")

start()
