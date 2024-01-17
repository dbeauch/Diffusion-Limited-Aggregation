ROOTCFLAGS = $(shell root-config --cflags)
ROOTLIBS   = $(shell root-config --libs)
ROOTGLIBS  = $(shell root-config --glibs)
ROOTFLAGS   = $(ROOTCFLAGS) $(ROOTLIBS) $(ROOTGLIBS) 
CXXFLAGS_OPT  = $(ROOTCFLAGS) -Wall -O3
CXXFLAGS_DBG = $(ROOTCFLAGS) -Wall -g
LDFLAGS    = $(ROOTLIBS) $(ROOTGLIBS)

GSLFLAGS     = -lgsl -lgslcblas

CXXFLAGS = $(CXXFLAGS_OPT)

default: projGSL

debug: CXXFLAGS = $(CXXFLAGS_DBG)
debug: projGSL


projGSL:  projGSL.cpp
	$(GXX) $(CXXFLAGS) -o projGSL projGSL.cpp $(LDFLAGS) $(GSLFLAGS)


clean:
	rm -f projGSL projGSL.root *~
