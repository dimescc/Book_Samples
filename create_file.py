
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
    f.write("$ docker build -t ")
    f.write(appli)
    f.write(" .\n")
    f.write("\nRun the container\n")
    f.write("$ docker run --rm -p ")
    f.write(porti)
    f.write(":5000 ")
    f.write(appli)
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
    f.write("  \"name\": \"")
    f.write(appli)
    f.write("\",\n")
    f.write("  \"description\": \"")
    f.write(desc)
    f.write("\",\n")
    f.write("  \"version\": \"")
    f.write(vers)
    f.write("\",\n")
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
    f.write("Import ")
    f.write(impor)
    f.write("\n\ndef ")
    f.write(func)
    f.write(": \n")
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
    f.write("  name: ")
    f.write(appli)
    f.write("\nspec:\n")
    f.write("  containers:\n")
    f.write("  - name: ")
    f.write(appli)
    f.write("\n    image: ")
    f.write(appli)
    f.write(":")
    f.write(vers)
    f.write("\n    ports:")
    f.write("\n    - containerPort: ")
    f.write(port)
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
    f.write("        image: ")
    f.write(appli)
    f.write(":")
    f.write(vers)
    f.write("\n        command: ['sh', '-c', 'echo \"Hello, Kubernetes!\" && sleep 3600']\n")   
    f.write("       restartPolicy: OnFailure\n")
    f.write("    # The pod template ends here")
    f.close()

# Latex File
elif typ == "6":
    typ = input("Document Type or Class (Book, Report, Letter, Article, ...): ")
    c1 = input("Chapter 1: ")
    c2 = input("Chapter 2: ")
    filei = "C:\\MYFiles_TPc\\" + typ_chosen["6"]
    f = open(filei, "w") # a = append / anfügen, w = Overwrite / löschen, neu schreiben
    f.write("Document Type ")
    \documentclass[12pt, letterpaper, twoside]{article}
\usepackage[utf8]{inputenc}

\title{First document}
\author{Hubert Farnsworth \thanks{funded by the Overleaf team}}
\date{February 2014}

\begin{document}

\begin{titlepage}
\maketitle
\end{titlepage}

In this document some extra packages and parameters
were added. There is an encoding package
and pagesize and fontsize parameters.

\end{document}

    f.close()
		
			

 
 
#  Shell Script File
elif typ == "7":
    print(typ_chosen["7"])

# Batch File
elif typ == "8":
    print(typ_chosen["8"])

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
