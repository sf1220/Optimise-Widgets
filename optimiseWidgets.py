import digraphs
import csv
import sys

# You can define some helper functions here if you like!

def optimiseWidgets(filename):

   with open(filename, "r") as csv_file:
      csv_reader = csv.reader(csv_file)
      next(csv_reader)
      my_list = list(csv_reader)

   input = [el[2] for el in my_list]

   output = [el[3] for el in my_list]

   rawMats = input + output

   V = list(set(rawMats))

   inOut = [(input[i], output[i]) for i in range(0, len(input))]

   weights = [el[4] for el in my_list]

   w = {}
   for key in inOut:
      for value in weights:
         w[key] = int(value)
         weights.remove(value)
         break

   E = set(w.keys())

   v = ""


   def hasInEdge(V, E, v):
      return len(digraphs.N_in(V, E, v)) != 0

   def hasOutEdge(V, E, v):
      return len(digraphs.N_out(V, E, v)) == 0

   for x in range(len(V)):
      v = V[x]
      start = hasInEdge(V, E, v)
      if start != True:
         s = v


   for x in range(len(V)):
      v = V[x]
      end = hasOutEdge(V, E, v)
      if end == True:
         d = v


   machineSettings = digraphs.maxFlow(V, E, w, s, d)
   return machineSettings


# TEST HARNESS
# The following will be run if you execute the file like python3 widget_n1234567.py widgetsamplefile.csv
# Your solution should not depend on this code.
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please provide a filename for the input CSV file.")
        sys.exit(1)

    filename = sys.argv[1]
    solution = optimiseWidgets(filename)
    print(solution)
