import sys

class Zero2OnePlugin:
    def input(self, filename):
        self.infile = open(filename, 'r')

    def run(self):
        pass

    def output(self, filename):
       outfile = open(filename, 'w')

       line = self.infile.readline()
       outfile.write(line)

       for line in self.infile:
          contents = line.strip().split('\t')
          outfile.write(contents[0])
          outfile.write('\t')
          for i in range(1,len(contents)):
              if (float(contents[i]) == 0):
                  outfile.write("1")
              else:
                  outfile.write(contents[i])
              if (i == len(contents)-1):
                  outfile.write("\n")
              else:
                  outfile.write("\t")
