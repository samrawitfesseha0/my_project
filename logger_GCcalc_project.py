'''
Created on Apr 26, 2023

@author: Samrawit Fesseha
'''
'''
project_name=GCcalc
For the GC calc project: Add a logger method and calculate GC frequency for all miRNA in human, mouse and rat in the mature sequence''' 
#-f "C:\Users\user\AP\day1\data\mature.fa" -s hsa
#-f "C:\Users\user\AP\day1\data\mature.fa" -s mmu
#-f "C:\Users\user\AP\day1\data\mature.fa" -s rno

import json
import sys
import os
from locale import atof, setlocale, LC_NUMERIC
from datetime import datetime
import hashlib
import logging
import sequence
from pathlib import Path
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter




__all__ = []
__version__ = 0.1
__date__ = '2023-04-11'
__updated__ = '2022-04-11'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

def initLogger(md5string):

    ''' setup log file based on project name'''
    projectBaseName = ""

    projectBaseName = Path(fastaFile).stem

    now = datetime.now()
    dt_string = now.strftime("%Y%m%d_%H%M%S")
    logFolder = os.path.join(os.getcwd(), "logfiles")
    if not os.path.exists(logFolder):
        print("--log folder <" + logFolder + "> doesn't exist, creating")
        os.makedirs(logFolder)
    logfileName = os.path.join(logFolder, projectBaseName + "__" + dt_string + "__" + md5string +".log")
    handler = logging.StreamHandler(sys.stdout)
    logging.basicConfig(level=logging.DEBUG)

    fileh = logging.FileHandler(logfileName, 'a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileh.setFormatter(formatter)

    log = logging.getLogger()  # root logger
    log.setLevel(logging.DEBUG)
    for hdlr in log.handlers[:]:  # remove all old handlers
        log.removeHandler(hdlr)
    log.addHandler(fileh)      # set the new handler
    log.addHandler(handler)
    logging.info("+" + "*"*78 + "+")
    logging.info("project log file is <" + logfileName + ">")
    logging.info("+" + "*"*78 + "+")
    logging.debug("debug mode is on")

def parseArgs(argv):
    
    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    #program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = ''
    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("-f", "--fasta_file", dest="fastafile", action="store", help="fasta file for which you want to calc GC% [default: %(default)s]")
        parser.add_argument("-s", "--species_code", dest="speciescode", action="store", help="three character species code [default: %(default)s]")

 # Process arguments
        args = parser.parse_args()
        
        global fastaFile
        global speciesCode

        fastaFile = args.fastafile
        speciesCode = args.speciescode

        if fastaFile:
            print("fasta file is <" + fastaFile + ">")

        if speciesCode:
            print("speciesCode is <" + speciesCode + ">")

    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception as e:
        print(e)
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
    

def readFastaFile(filename):
    '''
    load specified fasta file
    :param self:
    :return:
    '''
    global headerLines
    global sequenceLines
    # load the fasta lines into a list
    try:
        fFA = open(filename, 'r')
        fastaLines = fFA.readlines()
        fFA.close()
    except Exception as e:
        raise(e)

    headerLines = []
    headerLine = ""
    sequenceLines = []
    sequence = ""
    
    s = 0
    for fastaLine in fastaLines:
        if fastaLine[0] == '>':
            if s > 0 and headerLine.startswith(speciesCode):
                headerLines.append(headerLine)
                sequenceLines.append(sequence)
                sequence = ""
            headerLine = fastaLine[1:].strip()
        else:
            sequence = sequence + fastaLine.strip()
        s += 1
    if headerLine.startswith(speciesCode):
        headerLines.append(headerLine)
        sequenceLines.append(sequence)
    return len(headerLines)
    
def calcAverageGCPercent():
    '''
    calculate GC percent for each sequence and return the average value
    :return:
    '''
    
    totalGCPercent = 0
    sCount = 0
    for seqLine in sequenceLines:
        seq = sequence.Sequence(headerLines[sCount], seqLine)
        seq.calcGC()
        print("for sequence <" + seq.getHeaderLine() + "> GC% is <" + str(100.0*seq.getGCPercent()) + ">")
        totalGCPercent = totalGCPercent + seq.getGCPercent()
    return totalGCPercent/len(sequenceLines)



def main(argv=None): # IGNORE:C0111

    #setlocale(LC_NUMERIC, 'no_NO')
    if argv is None:
        argv = sys.argv
    parseArgs(argv)  
    md5String = hashlib.md5(b"CBGAMGOUS").hexdigest()    
    initLogger(md5String) 
    global filename
    filename = r"C:\Users\user\AP\day1\data\mature.fa"
    n = readFastaFile(filename)
    print("found <" + str(n) + "> sequences")
    avGCPercent = calcAverageGCPercent()
    print("average GC % = <" + str(100.0*avGCPercent) + ">")




if __name__ == '__main__':

    sys.exit(main())
  
    
    
        
        
        
        
        