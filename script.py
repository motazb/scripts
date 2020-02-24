#!/usr/bin/env python

def openfile(fname):
    import numpy
    import pandas as pd
    tmp_data = pd.read_csv(fname)
    data = tmp_data.to_numpy()
openfile('patientdata.csv')



def maxage(fname):
    import numpy
    import pandas as pd
    tmp_data = pd.read_csv(fname)
    data = tmp_data.to_numpy()
    age = data[:,4]
    age_max = numpy.max(age)
    print("The oldest patient is ", age_max, " years old.")
maxage('patientdata.csv')


print("\n")


def display(source, numlines = 3):
    print("Here is a preview of the file:")
    with open(source) as f:
        for i, line in enumerate(f):
            print(line.strip())
            if i == numlines:
                break
display('patientdata.csv')


print("\n")


def displaydict(source, numlines = 3):
    print("Here is a preview of the file in a dictionary")
    import csv
    with open(source) as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            print(dict(row))
            if i == numlines:
                break
displaydict('patientdata.csv')


print("\n")



def importgenderdata(source, output, gender):
    print("Here is a preview of the female patients only")
    import csv
    assert gender != "Female" or "Male", "Please ensure first letter of gender is capitalized"
    with open (source) as fr:
        reader = csv.DictReader(fr)
        header = reader.fieldnames
        with open (output, "w") as fw:
            writer = csv.DictWriter(fw, fieldnames = header, delimiter = ",")
            for row in reader:
                if row["sex"] == gender:
                    writer.writerow(row)
importgenderdata('patientdata.csv', 'femaledata.csv', 'Female')
with open('patientdata.csv') as f:
    for i, line in enumerate(f):
        print(line.strip())
        if i == 3:
            break

print("\n")



def hist(source):
    import numpy
    import pandas as pd
    tmp_data = pd.read_csv(source)
    data = tmp_data.to_numpy()
    import matplotlib.pyplot as plt
    ages = data[:,4]
    x = [ages]
    plt.style.use('ggplot')
    plt.hist(x, bins = 10)
hist('patientdata.csv')
