import os
import re
import json

def main():
  rootdir = 'ENTER PATH HERE'
  final_list = []
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
	      for parameter in parameters:
                rips_dict = {}
                rips_dict['type'] = "_POST"
                rips_dict['parameter'] = parameter
                rips_dict['method'] = controller
                rips_dict['class'] = className
                #print rips_dict        
                final_list.append(rips_dict)
          else:
            pass
  print json.dumps(final_list)


def controllerParser(line):
  controller = line.split("(")[0].split()[2]
  parameters = []
  splitLine = line.split("(")[1].split()
  for item in splitLine:
    if '$' in item:
      item.split('$')
      parameters.append(re.sub('[$),(:]', '', item))
    else:
      pass
  return controller, parameters

if __name__ == '__main__':
  main()
