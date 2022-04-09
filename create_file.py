
# Super anleitung: https://www.w3schools.com/python/python_file_open.asp

print("Please chose:")
print("1 for a Docker file")
print("2 for a JSON")
print("3 for an ANSIBLE file")
print("4 for a Python script")
print("5 for a Kubernetes Pod")
print("6 for a LATEX code")
print("7 for a Shell script")
print("8 for a Batch script")
typ = input("9 for a Launcher Config file: ")
typ_chosen = {"1" : "DOCKER", "2" : "definition.JSON", "3" : "ANSIBLE.cfg", "4" : "script.py", "5" : "kuber_pod.yaml", "6" : "Latex.tex", "7" : "Shell.sh", "8" : "Script.bat", "9" : "launcher_config.xml"}



# Docker File
if typ == "1": 
    appli = input("Name of the application: ")
    porti = input("Running on which Server Port: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["1"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("# Befehle: https://github.com/LeCoupa/awesome-cheatsheets/blob/master/tools/docker.sh\n")
    f.write("# Create a local Docker container, Clone this repository first:\n\n")
    f.write("Build the docker container\n")
    f.write("$ docker build -t "); f.write(appli), f.write(" .\n")
    f.write("\nRun the container\n")
    f.write("$ docker run --rm -p "); f.write(porti); f.write(":5000 "), f.write(appli)
    f.write("\n\nTo add more instances, vary the public port number before the colon:\n")
    f.write("$ docker run --rm -p 81:5000 blockchain\n")
    f.close()

# JSON File
elif typ == "2":
    appli = input("Name of the application: ")
    desc = input("Please insert a useful description: ")
    vers = input("Which SW Version: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["2"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("{\n")
    f.write("  \"name\": \""); f.write(appli); f.write("\",\n")
    f.write("  \"description\": \""); f.write(desc); f.write("\",\n")
    f.write("  \"version\": \""); f.write(vers); f.write("\",\n")
    f.write("  \"private\": true,\n")
    f.write("  \"scripts\": {\n")
    f.write("    \"start\": \"node ./bin/www\"\n")
    f.write("  },\n")
    f.write("  \"dependencies\": {\n")
    f.write("    \"express\": \"~4.12.2\",\n")
    f.write("    \"jade\": \"~1.9.2\"\n")
    f.write("  }\n")
    f.write("}")
    f.close()

# Ansible Config File
elif typ == "3":
    print(typ_chosen["3"])

# Python Script
elif typ == "4":
    impor = input("What to import? ")
    func = input("Function to define: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["4"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("\n# Welcome to the Python script. Copyright T. Puchegger (DIMESCC) 2022 \n\n")
    f.write("Import "); f.write(impor)
    f.write("\n\ndef "); f.write(func); f.write(": \n")
    f.write("   erg = argA * argB \n")
    f.write("   print(erg)\n\n")
    f.write(func)
    f.close()

# Kubernetes Pod and Job
elif typ == "5": 
    appli = input("How is the application called? ")
    vers = input("Specify the SW Version: ")
    port = input("Running on which port? ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["5"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("\nPod creation:\n")
    f.write("apiVersion: v1\n")
    f.write("kind: Pod\n")
    f.write("metadata:\n")
    f.write("  name: "); f.write(appli)
    f.write("\nspec:\n")
    f.write("  containers:\n")
    f.write("  - name: "); f.write(appli)
    f.write("\n    image: "); f.write(appli); f.write(":"); f.write(vers)
    f.write("\n    ports:")
    f.write("\n    - containerPort: "); f.write(port)
    f.write("\n\n # To create the Pod shown above, run the following command:")
    f.write("\n # kubectl apply -f https://k8s.io/examples/pods/simple-pod.yaml")
    f.close()
    f = open("C:\\MYFiles_TPc\\kuber_job.py", "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("# The sample below is a manifest for a simple Job with a template that starts one container. The container in that Pod prints a message then pauses.\n\n")
    f.write("apiVersion: batch/v1\n")
    f.write("kind: Job\n")
    f.write("metadata:\n")
    f.write("  name: hello\n")
    f.write("spec:\n")
    f.write("  template:\n")
    f.write("    # This is the pod template\n")
    f.write("    spec:\n")
    f.write("      containers:\n")
    f.write("      - name: hello\n")
    f.write("        image: "); f.write(appli); f.write(":"); f.write(vers)
    f.write("\n        command: ['sh', '-c', 'echo \"Hello, Kubernetes!\" && sleep 3600']\n")   
    f.write("       restartPolicy: OnFailure\n")
    f.write("    # The pod template ends here")
    f.close()

# Latex File
elif typ == "6":
    typ = input("Document Class (Article, report, Letter, Book, ...): ")
    tit = input("Title of the Document: ")
    dat = input("Date for the Document: ")
    aut = input("Author of the Document: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["6"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("% compiler: https://latex.informatik.uni-halle.de/latex-online/latex.php")
    f.write("\n\\documentclass[12pt, letterpaper, twoside]{"); f.write(typ); f.write("}\n")
    f.write("\\usepackage[utf8]{inputenc}\n")
    f.write("\\usepackage{graphicx}\n")
    f.write("\\usepackage{pythontex}\n\n")
    f.write("\\newcommand{\pymultiply}[2]{\py{#1*#2}}\n\n")
    f.write("\\begin{document}\n\n")
    f.write("\\title{"); f.write(tit); f.write("}\n")
    f.write("\\author{"); f.write(aut); f.write("}\n")
    f.write("\\date{"); f.write(dat); f.write("}\n\n")
    f.write("\\maketitle\n\n")
    f.write("\\begin{abstract}\n")
    f.write("The abstract text goes here. Please use any feasable function available.\n")
    f.write("\\end{abstract}\n\n")  
    f.write("\\section{Introduction}\n")
    f.write("Here is the text of your introduction.\n\n")
    f.write("\\section{Main Topic}\n")
    f.write("This is the text to the document which can be edited later...\n\n")
    f.write("\\begin{pycode}\n")
    f.write("print(\"Python says Hello!\n")
    f.write("\\end{pycode}\n\n")
    f.write("Here some output with pycode if availabel\n\n")
    f.write("$8 \\times 256 = \pymultiply{8}{256}$\n\n")
    f.write("\\section{Conclusion}\n")
    f.write("Write your conclusion here.\n\n")
    f.write("\\end{document}\n")
    f.close()			

 
 
#  Shell Script File
elif typ == "7":
    am = input("Name of the script to create? ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["8"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("\n# https://linuxhint.com/30_bash_script_examples/")
    f.write("\n\nGet arguments from command line with names\n\n")
    f.write("#!/bin/bash\n\n")
    f.write("for arg in \"$@\"\n")
    f.write("do\n")
    f.write("   index=$(echo $arg | cut -f1 -d=)\n")
    f.write("   val=$(echo $arg | cut -f2 -d=)\n")
    f.write("   case $index in\n")
    f.write("       X) x=$val;;\n\n")
    f.write("       Y) y=$val;;\n\n")
    f.write("*)\n")
    f.write("esac\n")
    f.write("done\n")
    f.write("((result=x+y))\n")
    f.write("echo \"X+Y=$result\"\n\n\n\n")
    f.write("# String combine samples\n")
    f.write("string1=\"Linux\"\n")
    f.write("string2=\"Hint\"\n")
    f.write("echo \"$string1$string2\"\n")
    f.write("string3=$string1+$string2\n")
    f.write("string3+=\" is a good tutorial blog site\"\n")
    f.write("echo $string3\n\n\n")
    f.write("# add two numbers\n")
    f.write("echo \"Enter first number\"\n")
    f.write("read x\n")
    f.write("echo \"Enter second number\"\n")
    f.write("read y\n")
    f.write("(( sum=x+y ))\n\n")
    f.write("echo \"The result of addition=$sum\"\n")
    f.write("\n")
    f.clsoe()
    

# Batch File
elif typ == "8":
    nam = input("Name of the script to create? ")
    filei = "C:\\MYFiles_TPc\\" + nam + "_" + typ_chosen["8"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("\necho off\n\n")
    f.write("")
    f.write("REM set VARIABLENNAME=empty                                   // Variable zuweisen \n")
    f.write("REM echo %VARIABLENNAME%  				                // Ausgabe der Variable \n")
    f.write("REM RENAME [Laufwerk:][Pfad]Dateiname1 Dateiname2             	// umbenennen von Files\n")
    f.write("REM set /p VARIABLENNAME=Wert               			// Variable abfragen \n")
    f.write("REM RENAME \\\\frequentis.frq\\vie\\data\\QM\\QM\\Admin\\W_Puchegger\\Meeting_Minutes\\Templates\\QFM21001_Template_for_Minutes.docx NEWNAME.docx\n")
    f.write("REM https://de.wikibooks.org/wiki/Batch-Programmierung:_Erweiterungen_unter_Windows_NT \n\n")
    f.write("")
    f.write("set PSP=empty  							// PSP Variable zuweisen\n")
    f.write("set ALIAS=empty  				      		// Projektname Variable zuweisen\n")
    f.write("set PM=empty                                            // Projektleiter Variable zuweisen\n")
    f.write("set WS=0				         			// Workspace Nr.\n")
    f.write("set JAMA=0		         					// JAMA ID\n\n")
    f.write("")
    f.write("set /p PSP=Eingabe von PSP (z.B. PTEA47)?:\n")
    f.write("set /p ALIAS=Kurzname (z.B. Noednett - nur EIN Wort! keine Leerzeichen!)?: \n")
    f.write("set /p PM=Wer ist Projektleiter?: \n")
    f.write("set /p WS=Welche Nr. hat der Workspace?: \n")
    f.write("set /p JAMA=JAMA ID des Projektes?: \n\n")
    f.write("start iexplore http://intranet/SearchCenter/Pages/ProjectsResults.aspx?k=%PSP%\n")
    f.write("")
    f.write("C:\\Users\\pucheggt\\\"OneDrive - Constantia Flexibles\"\\Desktop\\open.bat %PSP% %ALIAS% %PM% %WS% %JAMA%\n\n")
    f.write("")
    f.write("")
    f.write("")
    f.write("REM im open.bat file:\n")
    f.write("REM Parameter Reihenfolge: %PSP% (%1) %ALIAS% (%2) %PM% (%3) %WS% (%4) %JAMA% (%5)\n")
    f.write("")
    f.write("REM SET \"par1=%1\"\n")
    f.write("REM SET \"par1=%2\"\n")
    f.write("")
    f.write("REM echo %par1%\n")
    f.write("REM echo %par1%\n")
    f.close()



# Launcher config File
elif typ == "9":
    impo = input("File to import to the Launcher config? ")
    group = input("Which group should be created first: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["9"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("\n<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n\n")
    f.write("<items>\n\n")
    f.write("<!-- Import of Remote Config Files -->\n")
    f.write("<import>\n")
    f.write(impo)
    f.write("</import>\n\n")
    f.write("   <group>\n")
    f.write("   <tag>")
    f.write(group)
    f.write("</tag>\n")
    f.write("       <item>\n")
    f.write("           <name>ITEM</name>\n")
    f.write("           <url>http://</url>\n")
    f.write("       </item>\n")
    f.write("   </group>")
    f.write("</items>")
    f.close()

# Break in Case of wrong input!
else:
    print("Wrong Input, Cancel!")






""" File operationen
f = open("demofile2.txt", "a") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
f.write("Now the file has more content!")
f.close()

f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()
"""



""" eine Funktion um ein Github file zu öffnen
from __future__ import annotations
from yaml import safe_load
from ansible.release import __codename__


def main():
    with open('.github/RELEASE_NAMES.yml') as f:
        releases = safe_load(f.read())

    # Why this format?  The file's sole purpose is to be read by a human when they need to know
    # which release names have already been used.  So:
    # 1) It's easier for a human to find the release names when there's one on each line
    # 2) It helps keep other people from using the file and then asking for new features in it
    for name in (r.split(maxsplit=1)[1] for r in releases):
        if __codename__ == name:
            break
    else:
        print('.github/RELEASE_NAMES.yml: Current codename was not present in the file')


if __name__ == '__main__':
    main()

"""
