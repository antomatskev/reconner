import os

REPORT_FILE = "vuln.nmap"

# dir = input("Enter directory with reports: ")
dir = "subs"

files = []
if os.path.isdir(dir):
	print(f"Composing reports from {dir}...")
	for d in os.walk(dir):
		if 0 < len(d) <= 3 and len(d[1]) == 0:
			report = d[0] + "/" + d[2][1]
			files.append(report)
else:
	print(f"{dir} not found")

divider = "====================================\n"
reports = []
final_rep = open("final_report.nmap", "w")
for f in files:
	with open(f) as report:
		final_rep.write(divider)
		final_rep.write(f.split("/")[1])
		final_rep.write("\n")
		final_rep.write(divider)
		final_rep.write(report.read())

final_rep.close()
print("Your report is ready. See final_report.nmap")
