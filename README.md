# :desktop_computer: Projet “Automatisation des tâches d’administration système”
Name of module : apache_analyser.py

Contributors : WONG Hoe Ziet & BIN AZMI Adam

# :open_book: Overview
This is a project of the module "Automatisation of System Administration Tasks" for the course of Diplôme Universitaire Technologie (DUT) Réseaux & Télécommunications.

The main function of the project is to analyse the access log file of an Apache server. The project is consisted of functions that are built to be able to inspect and analyse the data extracted from the log file and provide insights to client notably in the **security and commercial point of view**. The details and explanation of each the functions can be found below. The project also contains a simple Command Line Interface (CLI) that will facilitate the usage of the functions.

# :adult: Targetted User
Our targetted audience is the mainly the user of Apache server, specifically the server adminstrator or development team. This program can also eventually serve as model for other server who uses the same logging format.

# :gear: Installation
The package of the project will be available on PyPi soon after the complete structuring and validation. Stay tuned!

# :pencil: Usage
In the version 1.0.0 of this module, it contains a total of 10 functions that are conceived to facilitate the analysis of a running Apache server. Thanks to our CLI you can choose whichever functions that you wish. 

**Note : You will have to use "option --a" when running the code for the first time to convert the file into the format of JSON**
  
  - ### 1. convert_json (option --a)
    This function is used to convert a log file to json format. **This function must be used when running the module for the first time.**
   ```ruby
   apache_analyser.py path/to/your/log/file --a
   ```
  
 - ### 2. count_os (option --b)
    This function will help to detect the exploitation system (OS) used by clients. It generates percentage and graph showing the usage of each OS.
  ```ruby
  apache_analyser.py path/to/your/log/file --b
  ```
  
  - ### 3. average_size (option --c)
     It helps to calculate the average size of objects requested by clients. On top of that, it also provides the maximum and minimum size of objects requested. This allow us  to anticipate the traffic on the server, adapt the contains and adapt the bandwidth of the network according to the calculation.
  ```ruby
  apache_analyser.py path/to/your/log/file --c
  ```
  
  - ### 4. trafic_du_jour (option --d)
    This function is used to track the volume of visitors of the day, allowing us to monitor the current traffic on the server.
  ```ruby
  apache_analyser.py path/to/your/log/file --d
  ```
  
  - ### 5. count_method (option --e)
     With this function, we can observe and analysis the request methods used by the visitors. The analyse is carried on 4 most common request methods : GET, POST, HEAD and PUT. It also generates percentage and graph to provide a clearer representation.
  ```ruby
  apache_analyser.py path/to/your/log/file --e
  ```
  
 -  ### 6. heure_creuse (option --f)
     This function allow us to identify the peak hour on a server. This is undoubtedly crucial from the **commercial point of view**. For example, it will help to provide an insight on the best time to publish contains on a website.
  ```ruby
  apache_analyser.py path/to/your/log/file --f
  ```
  
 -  ### 7. count_response (option --g)
      This function will collect the data on HTTP Response Code. It will list 10 most common response code issued on the server along with their frequencies. From the **security point of view**, this function can serve as an red flag, providing early info to prevent attacks or dysfunctions on the server. Code in the range of 400 and 500 can potentially implicates security concern (loopholes for hacker) especially if the frequency is high. It also comes with percentage and graph interpretations.
  ```ruby
  apache_analyser.py path/to/your/log/file --g
  ```
  
 -  ### 8. analyse_ip_addr (option --i)
      This function will help to provide an analyse on the remote IP address or the IP address of clients. It is valuable from the **security point of view** as a repetitive IP address may possibly be a thread to the server. Combine with the data from other functions, a conclusion can certainly be deduced. 
  ```ruby
  apache_analyser.py path/to/your/log/file --i
  ```
  
-   ### 9. analyse_doc_type (option --j)
      This function is used to analyse the type of document requested by clients. The top 10 types of documents will be presented in the form of numbers, percentage and graph. By knowing the document type, we can study the general behaviour of client and adapt our contents following the trends.
  ```ruby
  apache_analyser.py path/to/your/log/file --j
  ```
  
  - ### 10. count_browser (option --k)
      This function will help to collect information of the browser used by clients. Indirectly, this can be exploited to strengthen commercialisation. For example, the advertissements can be posted more on certain browser with high traffic.
  ```ruby
  apache_analyser.py path/to/your/log/file --k
  ```
  
-  ### 11. Manual (option -h / --help)
      This option provides you with a mini manual on how to choose the options
  ```ruby
  apache_analyser.py path/to/your/log/file -h
  ```
 
  ```ruby
  apache_analyser.py path/to/your/log/file --help
  ```
  
 - ### 12. Version (option -V/ --version)
     This option will show you the current version of the module
  ```ruby
  apache_analyser.py path/to/your/log/file -V
  ```
  
  ```ruby
  apache_analyser.py path/to/your/log/file --version
  ```
  
# :fountain_pen: Code Style

[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

The module is written in compliant with the conventions of PEP8


# :lady_beetle: Reporting Bugs

Teamwork is the key, please report at https://github.com/Zac-not-Zack/apache_analyser/issues if you come across any bug.


# :warning: Licence

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)

MIT License

Copyright (c) 2021 Wong Hoe Ziet & Adam Bin Azmi


