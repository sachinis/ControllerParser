import os
import re

def main():
  rootdir = 'ENTER PATH HERE'
  for root, subFolders, files in os.walk(rootdir):
    for filename in files:
      fname = os.path.join(root,filename)
      with open(fname) as f:
        for line in f:
          if line.startswith("class"):
            className = line.split()[1]
          if 'public function __construct(' in line:
            pass
          elif 'public function' in line:
            if '$' in line:
              controller,parameters = controllerParser(line)
              print "Class Name: %s"%(className)
              print "Controller: %s"%(controller)
              print "Parameter(s): %s"%(parameters)
              print '\n'
          else:
            pass

def controllerParser(line):
  controller = line.split("(")[0].split()[2]
  var = []
  splitLine = line.split("(")[1].split()
  for item in splitLine:
    if '$' in item:
      item.split('$')
      var.append(re.sub('[$),(:]', '', item))
    else:
      pass
  return controller, var

if __name__ == '__main__':
  main()
