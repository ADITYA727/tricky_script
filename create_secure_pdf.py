import PyPDF2 as p,os
output = p.PdfFileWriter()
input_stream = p.PdfFileReader(open("C:\\Users\\hp\\Desktop\\work_on_ml\\grph\\foo.pdf", "rb"))

for i in range(0, input_stream.getNumPages()):
    output.addPage(input_stream.getPage(i))

outputstream = open("C:\\Users\\hp\\Desktop\\work_on_ml\\grph\\foo1.pdf", "wb")

output.encrypt("mypass", use_128bit=True)
output.write(outputstream)
outputstream.close()
