# Notes for Week 1 - ICT in healthcare

## Session 1
* Introducing everyone
* Schedule for the three-week guest teaching
    * Week 1 - ICT in healthcare
        * Technologies in ICT
        * Stakeholders in healthcare
        * Python basics and examples
    * Week 2 - health information system and eHealth
        * Concepts
        * Tools
        * Databases, SQL and NoSQL
    * Week 3 - Data analytics for big data in healthcare
        * Workflows in data analytics
        * Types of analysis (correlation, survival & predictive modelling)
        * Business intelligence
* Important concepts 
    * Plagiarism
        * A form of academic misconduct
        * Using contents from other sources but without proper citations
        * Can involve copyright or legal issues
        * Self-plagiarism: a special form of plagiarism that someone uses his / her own work without proper citations while the copyright has shifted to a third party (e.g. the publisher).
    * Citation
        * Multiple [styles](https://www.scribbr.com/citing-sources/citation-styles/) are available. Typically a journal will specify which style to use.
        * Use a citation software such as [EndNote](https://endnote.com/) (paid) [Mendeley](https://www.mendeley.com/) (free) to help manage the citations.
    * Ethics
        * Medical data are highly sensitive. The use of medical data is regulated by [laws](https://www.nhmrc.gov.au/applicable-laws-and-obligations). 
        * Personal privacy is protected by law [Privacy Act 1988](https://www.myhealthrecord.gov.au/for-healthcare-professionals/howtos/recognise-your-privacy-and-security-obligations).
        * When accessing medical data, one must get the ethics approval from a committee. The considerations of the ethics is summarised [here](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1906611/).
        * Research that involves **human** is regulated by the [National Statement on Ethical Conduct in Human Research 2007](https://www.nhmrc.gov.au/about-us/publications/national-statement-ethical-conduct-human-research-2007-updated-2018). The committee for human-related ethics is often referred as the Human Research Ethics Committee (HREC). Typically, consents also need to be obtained from the participants to use their data.
        
## Session 2
* The fields of healthcare
    * Perspective 1
        * Clinical vs research
    * Perspective 2:
        * Diagnosis, treatment and management
    * Stakeholders
        * Doctors
        * Patients / recipients
        * Researchers
        * Vendors (equipments)
        * Pharmaceutical companies (drugs)
* Structure of ICT applications
    * Front-end
        * What the user sees
        * Technologies
            * Web pages
            * Mobile applications
            * Desktop applications
                * Command line interface
                * Graphical user interface
    * Back-end
        * How the system work behind the scene
        * Technologies
            * Databases
            * Network and routing
            * Server and deployment in a large scale

## Session 3
* Install Python
    * Any version after 3.7.0 will do
    * Navigate to https://www.python.org
    * Download the installer
    * Install to `C:\python37`

## Session 4 - 6
* Launch Python
    * Start menu -> IDLE
* Python basics
    * Assignment: use `=` to assign a value to a variable

        ```python
        a = 1
        b = 2
        c = 3.14
        ```
    
    * Comments: commands starting with an `#` are comments. They won't be executed.

        ```python
        # This is a comment
        # Assign 3.14 to pi
        pi = 3.14
        ```
    * Inspect: use `print` to 

        ```python
        print('The value of a is', a)
        print('The value of b is', b)
        print('The values of c is', c)
        ```
    * Strings: a data type to hold characters. Use single quotes or double quotes to define.

        ```python
        s = "This is a string"
        print(s)
        ```

    * String methods: the functions attached to a string object. They are handy to achieved common tasks for strings.

        ```python
        print(s.title())
        print(s.center(80, '#'))
        print(s.split())
        ```

    * Index / slicing: get a subset of a sequential object such as a string. The index starts at 0 not 1. So the first item should be item 0.

        ```python
        s2 = 'I love this game'
        # To get the word "game"
        # It starts at index 12
        print(s2[12:]) # 12: means index 12 to the end
        ```
    * Dictionaries: a data type for key - value pairs. The user can use the key to search for the corresponding value.

        ```python
        d = {'subject': 'Health informatics'}
        d['length'] = '6 sessions'
        d['language'] = 'python'
        ```

    * Get input: use `input()` to get input from the user.

        ```python
        # The answer will be stored in name
        name = input('What is your name? ')
        ```

    * Save data to file: use `open()` to open a file so that data can be written.

        ```python
        f = open('C:/test.txt', 'w') # 'w' means writing mode
        f.write('Health informatics`)
        f.close()
        ```

    * Read data from file: similarly, use `open()` to open a file, then read the data.

        ```python
        f = open('c:/test.txt', 'r') #'r' means reading mode
        content = f.read()
        print(content)
        ```

    * Utilise the functions in a module: use the `import` statement to include the module to the current session.
    
        ```python
        import json
        ```

    * Process data with JSON: use `json.dumps()` to convert a Python object to a string in JSON. Use `json.loads()` for the opposite conversion.

        ```python
        d = {
        'subject': 'Health informatics',
        'length': '6 sessions',
        'language': 'python'
        }
        
        d_json = json.dumps(d)

        # d_json is the data to be written on disk
        # Another program may read the data from disk, to reconstruct the original object
        d_recovered = json.loads(d_json)
        ```

* A command line interface (CLI) [example](./cli_demo.py) is available using the above Python components.

* The previous example can be further developed into a graphical user interface (GUI) program. In Python, `tkinter` is the default GUI package which is able to build native-looking GUI desktop applications. To learn more about `tkinter`, please read this [article](https://likegeeks.com/python-gui-examples-tkinter-tutorial/#Add-a-Menu-bar).
