def separateSkillsByLine(inFILE,outFILE):
    """Takes original standards.csv format and separates 
multiple skills per quiz onto separate lines."""

    f = open(inFILE, 'rU')
    f2 = open(outFILE, 'w')
    for line in f:
        info = line.strip().split(',')
        nameINFO = ','.join(info[:8])
        for STscore in info[8:]:
            data = STscore.split(':')
            skill = data[0].upper()
            f2.write(nameINFO + ',' + skill + ',' + data[1] + '\n')
    f.close()
    f2.close()


if __name__ == "__main__":
    import sys
    try:
        f = sys.argv[1]
        f2 = sys.argv[2]
    except:
        print "Usage: helper.py input output"
        sys.exit()
    separateSkillsByLine(f, f2)
    print "Done"
 
