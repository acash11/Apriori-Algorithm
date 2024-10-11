import Apriori
import sys

#Command line program for apriori.py
#To run: python run_apriori.py filename min_support_count(As a percentage)

if __name__ == "__main__":
    #print(sys.argv)
    assert len(sys.argv) == 3
    filename = str(sys.argv[1])
    min_support = int(sys.argv[2])

    print(Apriori.apriori(filename, min_support))