#!/usr/bin/env python3

import datetime
import os

from run import catalog_data
from reports import generate_report
from emails import generate_email, send_email


def pdf_body(input_for,desc_dir):
    """Generating a summary with two lists, which gives the output name and weight"""
    n = []
    w = []
    for item in os.listdir(desc_dir):
      filename=os.path.join(desc_dir,item)
      with open(filename) as f:
        line=f.readlines()
        weight=line[1].strip('\n')
        name=line[0].strip('\n')
        print(name,weight)
        n.append('name: ' +name)
        w.append('weight: ' +weight)
        print(n)
        print(w)
    new_obj = ""  # initializing the object
    # Calling values from two lists one by one.
    for i in range(len(n)):
        if n[i] and input_for == 'pdf':
            new_obj += n[i] + '<br />' + w[i] + '<br />' + '<br />'
    return new_obj

if __name__ == "__main__":
    description_directory = '/home/<student-username>/supplier-data/descriptions/'
    current_date = datetime.date.today().strftime("%B %d, %Y")
    title = 'Processed Update on ' + str(current_date)
    generate_report('/tmp/processed.pdf', title, pdf_body('pdf',description_directory))
    email_subject = 'Upload Completed - Online Fruit Store' 
    email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.' 
    msg = generate_email("automation@example.com", "<student-username>@example.com",
                         email_subject, email_body, "/tmp/processed.pdf")
    send_email(msg)