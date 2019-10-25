# PF-Alquimia_verification
This repo contains verification results from ParFlow-Alquimia tests

Results are located in .txt files in the individual test folders. All tests were run using the CrunchFlow geochemistry engine, except for isotherms\_1d, which contains 'crunch' and 'pflotran' folders. PF\_GetXY.py contains a python helper function to read the .txt files of these simulations. This function is hardcoded for the domain used here.

Original input scripts are located in the test folders (ParFlow, geochemical engine input and database). Also included is a TCL script to convert ParFlow's binary outputs to txt. Usage: "tclsh pfb\_to\_txt.tcl FileName.pfb"    
