import csv

with open('datosEjercicio1_remoto-recortado.csv', 'r', newline='') as csvfile:
    # handle header line, save it for writing to output file
    header = next(csvfile).strip("\n").split(",")
    reader = csv.reader(csvfile)
    results = list(filter(lambda row:  (row[5]).astype(str).str.contains('AlumnosRdto 1-1'), reader))
  

with open('datos-remoto-alumno1.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    for result in results:
        writer.writerow(result)