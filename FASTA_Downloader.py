#! python2

import urllib2


def downloader(IdValue):
    UID = IdValue.strip()
    FastaString1 = 'http://www.uniprot.org/uniprot/'
    FastaString2 = '.fasta?include=yes'
    FastaURL = FastaString1 + UID + FastaString2
    FastaPage = urllib2.urlopen(FastaURL)
    FastaData = FastaPage.read()
    OutFile = open(UID+'.txt', 'w')
    OutFile.write(FastaData)
    OutFile.close()


def main():
    InputFile = raw_input('File with list of UID values: ')
    with open(InputFile, 'r') as InputData:
        for i in InputData:
            print 'Downloading: ' + i
            downloader(i)

if __name__ == '__main__':
    main()
