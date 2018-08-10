
import csv
from collections import OrderedDict
import pickle
import json

with open('groundTruth.csv') as f:
	read = csv.reader(f, delimiter=',')
	b = {}
	a = []
	a.append(['label_index','label','filename','st_frame','end_frame'])
	for row in read:
		filename = row[1]
		st_frame = row[2]
		end_frame = row[3]
		label_index = row[4]
		label = row[5]
		a.append([row[4],row[5],row[1],row[2],row[3]])

with open('temp_out.csv','w') as f:
	writer = csv.writer(f)
	writer.writerows(a)

with open('temp_out.csv', 'r', newline='') as f_input:
    csv_input = csv.DictReader(f_input)
    data = sorted(csv_input, key=lambda row: (row['label_index']))

with open('sorted_index.csv', 'w', newline='') as f_output:    
    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)

with open('temp_out.csv', 'r', newline='') as f_input:
    csv_input = csv.DictReader(f_input)
    data = sorted(csv_input, key=lambda row: (row['filename']))

with open('sorted_video.csv', 'w', newline='') as f_output:
    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)

with open('sorted_video.csv', 'r') as infile, open('sorted_video_reordered.csv', 'a') as outfile:
    # output dict needs a list for new column ordering
    fieldnames = ['filename','label_index','label','st_frame','end_frame']
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    # reorder the header first
    writer.writeheader()
    for row in csv.DictReader(infile):
        # writes the reordered rows to the new file
        writer.writerow(row)

	
