import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep


class TestDriver(unittest.TestCase):
    def run_commands(self, driver, list_of_commands):
        ###################################################
        #
        #   Tiddlywiki          := tc-sidebar-scrollable, tc-story-river
        #   tc-story-river      := tc-tiddler-frame*
        #   tc-tiddler-frame    := data-tiddler-title="DrMobileHome" | data-tiddler-title="LoginPage"
        #   tc-tiddler-frame    := tc-tiddler-title, tc-tiddler-body
        #   tc-tiddler-body     := p*, tc-tab-set
        #
        #   tc-tab-set          := tc-tab-buttons | tc-tab-divider | tc-tab-content
        #   

        # List of command:
        # name: String Description of Step
        # test_element: step, results, verify
        # variable: unqiue name to store results of query, can be referenced in input
        # command: commands associated with test_element
        #           step:    attribute - name of a tag attribute, usually associate with elements of tiddler
        #                    className - name of a tag class name, usually associate with a named tiddler
        #                    tagName - html tag name
        #                    click - form element action or link action
        #           results: equal - compare variable with parameter
        #                    exists - (no parameter), input has results.
        #           verify:  equal, exists
        #           debug:   text - outputs the text results of the input
        # parameter: information neeed for command
        # input: variable to apply command
        #       initial variable: frame

        # List of commands
        # The List of Commands is a list of dictionaries.
        # Each dictionary has a set of keys, that the following code looks for
        #   keys            : value resprentation
        #   -----           : ------
        #   name            : names the command to distingush the different commands. Can be anything you want
        #   test_element    : Identifies the command as a Step, Results or Verify
        #   variable        : Is the name of the key that will store the results of the command in the results dictionary. 
        #                       Variable should be unqiue, unless you are overriding a variable.
        #                       Variables are used as inputs in following commands.
        #   command         : This is the action that is uses input, and parameter a qualifier.
        #                   :   Step Commands                                
        #                   :   --------
        #                   :   attribute       uses parameter to find an attribute of the input input 
        #                   :   classname       uses parameter as the classname in input, to find the html tag set with classname attribute
        #                   :   tagname         uses parameter as the html tag to search input for html tags names. (usually returns an list)
        #                   :   getListItem     will return an item in the list (input), based on the index (parameter, zero index)
        #                   :   click           if the input is list of buttons, it will activate the button, with index (parameter).
        #                   :   click_single    if the input is a single button, it will activate the button.
        #                   :   sendkeys        if the input is a text field, it will send the keys found in parameter to the text form element.
        #   parameter       : Parameter is what is being searched for in the input
        #   input           : Is the variable that contains the searchable data, usually the sub-section of an html page.
        #                       The input must be previously saved as a variable befor using it. 
        #                       The first variable/input is "frame"
        #  Example: [{"name":"Get Tiddler Body",   "test_element":"step",      "variable":"Enter",              "command":"className",  "parameter":"Enter",   "input":"frame"},
        #            {"name":"Get click Home  ",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":0,            "input":"Enter"},
        #            {"name":"End of Tests",         "test_element":""}]
        # The first finds the tag with the className of "Enter" in the variable frame, and set the resulting html tag to the Variable "Enter"
        # The next line causes the input tag "Enter" to be clicked. Saving the results of the command to be saved in "clickEnter"
        
        


        frame = driver.find_element_by_class_name("tc-tiddler-frame")
        results = {"frame":frame}

        for command in list_of_commands:
            sleep(.5)
            print(f"Running test {command['name']}")

            if command["test_element"] == "step":
                print(f"\t Test Step:", end="")
                
                if command["command"] == "attribute":
                    print(f"\t\tFinding attribute in html {command['parameter']}")
                    html_results = results[command["input"]].get_attribute(command["parameter"])
                    print(f"\t\t Results: {html_results}")
                    results[command["variable"]]=html_results

                elif command["command"] == "className":
                    print(f"\t\tFinding className in html {command['parameter']}")
                    html_results = results[command["input"]].find_element_by_class_name(command["parameter"])
                    print(f"\t\tResults: {html_results}")
                    results[command["variable"]]=html_results
 
                elif command["command"] == "tagName":
                    print(f"\t\tFinding tagName in html {command['parameter']}")
                    html_results = results[command["input"]].find_elements_by_tag_name(command["parameter"])
                    print(f"\t\tResults: {html_results}")
                    results[command["variable"]]=html_results
                
                elif command["command"] == "getListItem":
                    print(f"\t\tFinding tagName in html {command['parameter']}")
                    list_item = results[command["input"]][command["parameter"]]
                    print(f"\t\Liist Item: {list_item}")
                    results[command["variable"]]=list_item

                elif command["command"] == "click":
                    print(f"\t\tFinding click in html {command['parameter']}")
                    results[command["input"]][command["parameter"]].click()
                    results[command["variable"]]="clicked"

                elif command["command"] == "click_single":
                    print(f"\t\tFinding click in html {command['parameter']}")
                    results[command["input"]].click()
                    results[command["variable"]]="clicked"
                
                elif command["command"] == "sendkeys":
                    print(f"\t\tSetting text in html {command['parameter']}")
                    results[command["input"]].send_keys([command["parameter"]])
                    results[command["variable"]]=command["parameter"]
                #else:
                    #print(f"Command not found:\'{command['command']\'")

            ################### Results #################################
            elif command["test_element"] == "results":
                print(f"\tTest Results:")
                
                if command["command"] == "equal":
                    if results[command["input"]] == command["parameter"]:
                        print(f"\tResults are good {results[command['input']]} == {command['parameter']}")
                        results[command["variable"]]=False
                    else:
                        print(f"\tResults are bad {results[command['input']]} == {command['parameter']}")
                        results[command["variable"]]=True

                if command["command"] == "exists":
                    if results[command["input"]]:
                        print(f"\tResults are good")
                    else: 
                        print(f"\tResults are bad")

                if command["command"] == "compare":
                    if command["parameter"] in results[command["input"]].text:
                        print(f"\t String {command['parameter']} found in {results[command['input']].text}") 
                    else :
                        print(f"\t String {command['parameter']} NOT found in {results[command['input']].text}" )

            ################### Verify #################################
            elif command["test_element"] == "verify":
                print(f"\tTest Verification:")
                if command["command"] == "equal":
                    if results[command["input"]] == command["parameter"]:
                        print(f"\tResults are verified {results[command['input']]} == {command['parameter']}")
                        results[command["variable"]]=False
                    else:
                        print(f"\tResults are not verified {results[command['input']]} == {command['parameter']}")
                        results[command["variable"]]=True
                    assert command["parameter"] not in results[command["input"]] 

                if command["command"] == "exists":
                    if results[command["input"]]:
                        print(f"\t VERIFIED")
                    else: 
                        print(f"\tNOT VERIFIED")

                if command["command"] == "compare":
                    if command["parameter"] in results[command["input"]].text:
                        print(f"\t VERIFIED: String {command['parameter']} found in {results[command['input']].text}") 
                    else :
                        print(f"\t NOT VERIFIED: String {command['parameter']} NOT found in {results[command['input']].text}" )

            ################ DEBUG #####################################
            elif command["test_element"] == "debug":
                print(f"\tDebug info:")

                if command["command"] == "text":
                    print(f"\t\tText of {command['input']}: \n{results[command['input']].text}")
         
            else:
                print(f"Command not processed: {command['name']}-{command['test_element']}")

            print()


class LoadBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.Ie()
        #self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get("https://byui-cse.github.io/cse270-course/Labs/DrMobil.html")
        driver.find_element_by_class_name("tc-btn-invisible").click()

    def test_run(self):

        driver = self.driver
        self.assertIn("Dr Mobil", driver.title)

        # Variable:Frame contains the following
        # <div data-tiddler-title="LoginPage" data-tags="" class="tc-tiddler-frame tc-tiddler-view-frame tc-tiddler-exists ">
        # +<div class="tc-tiddler-title">
        # +<div class="tc-titlebar">
        # +<span class="tc-tiddler-controls">
        # -<div class="tc-tiddler-body tc-reveal"><p>
    	# Enter Username:<input type="text" class="userName"><br>  
	    # Enter Password: <input type="password" value="">
	    # <button class="Enter">Enter </button>
        Test_Verify_Login = [
            {"name":"Get UserName",   "test_element":"step",      "variable":"Name",              "command":"className",  "parameter":"userName",   "input":"frame"},
            # Notice that the variable:Name is not the input for the next line. 
            # Variable: Name contains <input type="text" class="userName"> from the variable name variable:frame.
            {"name":"Enter User Name Text",   "test_element":"step",      "variable":"",              "command":"sendkeys",  "parameter":"William",   "input":"Name"},
            {"name":"Get Enter button",   "test_element":"step",      "variable":"Enter",              "command":"className",  "parameter":"Enter",   "input":"frame"},
            {"name":"Click Enter button",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":0,            "input":"Enter"},
            {"name":"End of Tests",         "test_element":""}]
        addPatient = TestDriver()
        addPatient.run_commands(driver, Test_Verify_Login)        

        Test_Verify_Home_Function_Link = [
            {"name":"Get Title",          "test_element":"step",      "variable":"title",             "command":"attribute",  "parameter":"data-tiddler-title",   "input":"frame"},
            {"name":"Check Title",        "test_element":"results",   "variable":"title_results",     "command":"equal",      "parameter":"DrMobileHome",         "input":"title"},
            # Each test you need to get the body of the main tiddler.
            {"name":"Get Tiddler Body",   "test_element":"step",      "variable":"body",              "command":"className",  "parameter":"tc-tiddler-body",   "input":"frame"},
            {"name":"Check Body ",        "test_element":"results",   "variable":"body_results",      "command":"exists",     "parameter":"",                   "input":"body"},
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"body"},
            {"name":"Get tc-tab-content",   "test_element":"step",      "variable":"tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"},
            {"name":"Get tabs           ",   "test_element":"step",      "variable":"buttons",     "command":"tagName",         "parameter":"button",   "input":"tab_buttons"},
            # Notice the first link is 0
            {"name":"Get click Home  ",   "test_element":"step",      "variable":"click_H_",         "command":"click",         "parameter":0,            "input":"buttons"},
            {"name":"Debug tab_content    ",   "test_element":"debug",      "variable":"",                "command":"text",         "parameter":0,            "input":"tab_content"},
            {"name":"Verify Functions",         "test_element":"verify",   "variable":"verifyFunctionResults",     "command":"exists",      "parameter":"Functions",    "input":"tab_content"}, 
            {"name":"End of Tests",         "test_element":""}]
        homeFunction = TestDriver()
        homeFunction.run_commands(driver, Test_Verify_Home_Function_Link)

        Add_New_Patient = [
            
            # Each test you need to get the body of the main tiddler.
            {"name":"Get Tiddler Body",   "test_element":"step",      "variable":"body",              "command":"className",  "parameter":"tc-tiddler-body",   "input":"frame"},
            {"name":"Check Body ",        "test_element":"results",   "variable":"body_results",      "command":"exists",     "parameter":"",                   "input":"body"},
            #Within the frame with have a tab menu, containing tc-tab-button, and tc-tab-content.
            {"name":"Get home tc-tab-buttons",   "test_element":"step",      "variable":"home_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"body"},
            {"name":"Get tabs           ",   "test_element":"step",      "variable":"home_buttons",     "command":"tagName",         "parameter":"button",   "input":"home_tab_buttons"},
            # Notice the second link is 1.
            {"name":"Get click Patient  ",   "test_element":"step",      "variable":"click_PatientMenu_",         "command":"click",         "parameter":1,            "input":"home_buttons"},
            
            #tc_tab_content changed with the button click.
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"patient_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"}, 
            
            # Nested inside content we have another set of 
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"patient_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"patient_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"patient_buttons",     "command":"tagName",         "parameter":"button",   "input":"patient_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_AddPatient_",         "command":"click",         "parameter":0,            "input":"patient_buttons"},

            # Nested inside patient content, we have AddPatient
            {"name":"Get AddPatient contents",   "test_element":"step",      "variable":"patient_add_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"patient_tab_content"}, 
            {"name":"Get text fields field",   "test_element":"step",      "variable":"patient_add_id",              "command":"tagName",         "parameter":"input",   "input":"patient_add_tab_content"},
            {"name":"Get New Id text field",   "test_element":"step",      "variable":"newID",                       "command":"getListItem",  "parameter":0,   "input":"patient_add_id"},
            {"name":"Set New Id text field",   "test_element":"step",      "variable":"",                            "command":"sendkeys",  "parameter":"Patient C",   "input":"newID"},
            
            # Adding patient
            {"name":"Get buttons",   "test_element":"step",                 "variable":"patient_buttons",         "command":"tagName",         "parameter":"button",   "input":"patient_add_tab_content"},
            {"name":"Get Add Patient button",   "test_element":"step",      "variable":"Add_patient_button",         "command":"getListItem",  "parameter":0,   "input":"patient_buttons"},
            {"name":"Debug Add Patient button",   "test_element":"debug",      "variable":"",                       "command":"text",         "parameter":0,            "input":"Add_patient_button"},
            {"name":"Click Add Patient button",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":0,            "input":"Add_patient_button"},

            # Update patient information
            {"name":"Get text fields field",   "test_element":"step",      "variable":"patient_add_id",              "command":"tagName",         "parameter":"input",   "input":"patient_add_tab_content"},
            {"name":"Get First Name text field",   "test_element":"step",      "variable":"newID",                       "command":"getListItem",  "parameter":1,   "input":"patient_add_id"},
            {"name":"Set New Id text field",   "test_element":"step",      "variable":"",                            "command":"sendkeys",  "parameter":"John",   "input":"newID"},
            {"name":"Get Description text field",   "test_element":"step",      "variable":"newID",                       "command":"getListItem",  "parameter":2,   "input":"patient_add_id"},
            {"name":"Set Description text field",   "test_element":"step",      "variable":"",                            "command":"sendkeys",  "parameter":"Injured by fall",   "input":"newID"},

            {"name":"Get buttons",   "test_element":"step",                 "variable":"patient_buttons",         "command":"tagName",         "parameter":"button",   "input":"patient_add_tab_content"},
            {"name":"Get Done button",   "test_element":"step",      "variable":"Done_button",         "command":"getListItem",  "parameter":1,   "input":"patient_buttons"},
            {"name":"Click Done button",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":1,            "input":"Done_button"},

            {"name":"Debug tab_content    ",   "test_element":"debug",      "variable":"textoftab",                "command":"text",         "parameter":0,            "input":"patient_add_tab_content"},
            {"name":"Check Body ",        "test_element":"verify",   "variable":"body_results",      "command":"compare",     "parameter":"Patient C",                   "input":"patient_add_tab_content"},

            {"name":"End of Tests",         "test_element":""}]
        
        addPatient = TestDriver()
        addPatient.run_commands(driver, Add_New_Patient)

        Test_Verify_Diagonse = [
            {"name":"Get Tiddler Body",   "test_element":"step",      "variable":"body",              "command":"className",  "parameter":"tc-tiddler-body",   "input":"frame"},
            {"name":"Check Body ",        "test_element":"results",   "variable":"body_results",      "command":"exists",     "parameter":"",                   "input":"body"},
            #Within the frame with have a tab menu, containing tc-tab-button, and tc-tab-content.
            {"name":"Get home tc-tab-buttons",   "test_element":"step",      "variable":"home_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"body"},
            {"name":"Get tabs           ",   "test_element":"step",      "variable":"home_buttons",     "command":"tagName",         "parameter":"button",   "input":"home_tab_buttons"},
            {"name":"Get click Home  ",   "test_element":"step",      "variable":"click_Patient_",         "command":"click",         "parameter":1,            "input":"home_buttons"},
            #tc_tab_content changed with the button click.
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"patient_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"}, 
            
            # Nested inside content we have another set of 
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"patient_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"patient_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"patient_buttons",     "command":"tagName",         "parameter":"button",   "input":"patient_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_AddPatient_",         "command":"click",         "parameter":1,            "input":"patient_buttons"},


            # Nested inside patient content, we have AddPatient
            {"name":"Get Diagnosis contents",   "test_element":"step",      "variable":"diagnosis_add_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"patient_tab_content"}, 
            {"name":"Get Select Patient",   "test_element":"step",          "variable":"diagnosis_select_patient",         "command":"tagName",         "parameter":"select",   "input":"diagnosis_add_tab_content"},
            {"name":"Get First Name text field",   "test_element":"step",      "variable":"First Select",                       "command":"getListItem",  "parameter":0,   "input":"diagnosis_select_patient"},
            {"name":"Debug Select Patient   ",   "test_element":"debug",      "variable":"selectoptions",                "command":"text",         "parameter":0,            "input":"First Select"},

            {"name":"Get Select Options",   "test_element":"step",                 "variable":"diagnosis_select_patient_option",         "command":"tagName",         "parameter":"option",   "input":"First Select"},
            {"name":"Get First Name text field",   "test_element":"step",      "variable":"PatientC",                       "command":"getListItem",  "parameter":2,   "input":"diagnosis_select_patient_option"},
            #{"name":"Get First Name text field",   "test_element":"step",      "variable":"PatientC",                       "command":"getListItem",  "parameter":1,   "input":"diagnosis_select_patient_option"},
            {"name":"Click Add Patient button",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":0,            "input":"PatientC"},

            #With the select Content changed
            # Nested inside content we have another set of 
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"patient_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"},
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"patient_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"patient_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"patient_buttons",     "command":"tagName",         "parameter":"button",   "input":"patient_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_Monitor_",         "command":"click",         "parameter":1,            "input":"patient_buttons"},
            {"name":"Get Monitor contents",   "test_element":"step",      "variable":"monitor_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"patient_tab_content"}, 
 
            ############################################################################################################
            # Tempature
            ############################################################################################################
            #Get Patient Table
            {"name":"Get Patient Info",   "test_element":"step",          "variable":"monitor_tables",         "command":"tagName",         "parameter":"table",   "input":"monitor_tab_content"},
            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_table",   "command":"getListItem",     "parameter":0,   "input":"monitor_tables"},
            {"name":"Get Patient Info rows",   "test_element":"step",          "variable":"monitor_rows",    "command":"tagName",         "parameter":"tr",   "input":"monitor_table"},

            #Get row 0, Temperature row
            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":0,   "input":"monitor_rows"},
            {"name":"Get Patient Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Patient row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            {"name":"Get text fields field",   "test_element":"step",      "variable":"patient_add_id",              "command":"tagName",         "parameter":"input",   "input":"monitor_cell"},
            {"name":"Get New Id text field",   "test_element":"step",      "variable":"newID",                       "command":"getListItem",  "parameter":0,   "input":"patient_add_id"},
            # Update Temperature
            {"name":"Set New Id text field",   "test_element":"step",      "variable":"",                            "command":"sendkeys",  "parameter":"101",   "input":"newID"},

            ############################################################################################################
            #TODO Step 2: Add values the values of Heartbeat, O2, and BloodPressure of Patient C
            # For example
            ############################################################################################################
            
            ###########################################################################################################
            #tc_tab_content changed with the button click.
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"patient_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"}, 
            
            # Nested inside content we have another set of 
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"patient_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"patient_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"patient_buttons",     "command":"tagName",         "parameter":"button",   "input":"patient_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_Monitor_",         "command":"click",         "parameter":2,            "input":"patient_buttons"},

            {"name":"Get Monitor contents",   "test_element":"step",      "variable":"monitor_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"patient_tab_content"}, 

            {"name":"Get Select Patient",   "test_element":"step",          "variable":"diagnosis_select_patient",         "command":"tagName",         "parameter":"select",   "input":"monitor_tab_content"},
            {"name":"Get First Name text field",   "test_element":"step",      "variable":"First Select",                       "command":"getListItem",  "parameter":0,   "input":"diagnosis_select_patient"},
            {"name":"Debug Select Patient   ",   "test_element":"debug",      "variable":"selectoptions",                "command":"text",         "parameter":0,            "input":"First Select"},

            {"name":"Get Select Options",   "test_element":"step",                 "variable":"diagnosis_select_patient_option",         "command":"tagName",         "parameter":"option",   "input":"First Select"},
            {"name":"Get First Name text field",   "test_element":"step",      "variable":"PatientC",                       "command":"getListItem",  "parameter":2,   "input":"diagnosis_select_patient_option"},
            #{"name":"Get First Name text field",   "test_element":"step",      "variable":"PatientC",                       "command":"getListItem",  "parameter":1,   "input":"diagnosis_select_patient_option"},
            {"name":"Click Patient C",   "test_element":"step",      "variable":"clickEnter",         "command":"click_single",         "parameter":0,            "input":"PatientC"},

            #With the select Content changed
            # Nested inside content we have another set of 
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"patient_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"},
            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"patient_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"patient_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"patient_buttons",     "command":"tagName",         "parameter":"button",   "input":"patient_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_Monitor_",         "command":"click",         "parameter":2,            "input":"patient_buttons"},
            {"name":"Get Monitor contents",   "test_element":"step",      "variable":"monitor_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"patient_tab_content"}, 
            
            #Find Update Table
            {"name":"Get Patient Info",   "test_element":"step",          "variable":"monitor_tables",         "command":"tagName",         "parameter":"table",   "input":"monitor_tab_content"},
            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_table",   "command":"getListItem",     "parameter":0,   "input":"monitor_tables"},
            {"name":"Get Patient Info rows",   "test_element":"step",          "variable":"monitor_rows",    "command":"tagName",         "parameter":"tr",   "input":"monitor_table"},
            
            ####################################################################################
            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":0,   "input":"monitor_rows"},
            {"name":"Get Patient Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Patient row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            ####################################################################################
            # Step 3:#TODO Change Debug to Verify statement based on what was entered for Monitor Tempature Values
            ####################################################################################
            {"name":"Debug Temp cell value",   "test_element":"debug",      "variable":"temp_value",                "command":"text",         "parameter":0,            "input":"monitor_cell"},
            ####################################################################################

            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":1,   "input":"monitor_rows"},
            {"name":"Get Patient Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Patient row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            ####################################################################################
            # Step 3: TODO: Change Debug to Verify statement based on what was entered for Monitor Heartbeat Values
            ####################################################################################
            {"name":"Debug Temp cell value",   "test_element":"debug",      "variable":"temp_value",                "command":"text",         "parameter":0,            "input":"monitor_cell"},
            ####################################################################################


            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":2,   "input":"monitor_rows"},
            {"name":"Get Patient Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Patient row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            ####################################################################################
            #Step 3: TODO: Change Debug to Verify statement based on what was entered for Monitor O2 Values
            ####################################################################################
            {"name":"Debug Temp cell value",   "test_element":"debug",      "variable":"temp_value",                "command":"text",         "parameter":0,            "input":"monitor_cell"},
            ####################################################################################

            {"name":"Get Select Patient row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":3,   "input":"monitor_rows"},
            {"name":"Get Patient Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Patient row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            ####################################################################################
            #Step 3: TODO: Change Debug to Verify statement based on what was entered for Monitor Pressure Values
            ####################################################################################
            {"name":"Debug Temp cell value",   "test_element":"debug",      "variable":"temp_value",                "command":"text",         "parameter":0,            "input":"monitor_cell"},
            ####################################################################################


            {"name":"End of Tests",         "test_element":""}]

        diagonse = TestDriver()
        diagonse.run_commands(driver, Test_Verify_Diagonse)

        Order_Supplies = [
            {"name":"Get Tiddler Body",   "test_element":"step",      "variable":"body",              "command":"className",  "parameter":"tc-tiddler-body",   "input":"frame"},
            {"name":"Check Body ",        "test_element":"results",   "variable":"body_results",      "command":"exists",     "parameter":"",                   "input":"body"},
            #Within the frame with have a tab menu, containing tc-tab-button, and tc-tab-content.
            {"name":"Get home tc-tab-buttons",   "test_element":"step",      "variable":"home_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"body"},
            {"name":"Get tabs           ",   "test_element":"step",      "variable":"home_buttons",     "command":"tagName",         "parameter":"button",   "input":"home_tab_buttons"},
            {"name":"Get click Home  ",   "test_element":"step",      "variable":"click_Communicate",         "command":"click",         "parameter":2,            "input":"home_buttons"},
            #tc_tab_content changed with the button click.
            {"name":"Get patient tc-tab-content",   "test_element":"step",      "variable":"Communicate_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"body"},

            {"name":"Get tc-tab-buttons",   "test_element":"step",      "variable":"communicate_tab_buttons",     "command":"className",  "parameter":"tc-tab-buttons",   "input":"Communicate_tab_content"},
            {"name":"Get PatientMenu Tabs",   "test_element":"step",      "variable":"communicate_buttons",     "command":"tagName",         "parameter":"button",   "input":"communicate_tab_buttons"},
            {"name":"Get click AddPatient tab",   "test_element":"step",      "variable":"click_OrderSupplies",         "command":"click",         "parameter":1,            "input":"communicate_buttons"},

            {"name":"Get Monitor contents",   "test_element":"step",      "variable":"OrderSupplies_tab_content",     "command":"className",  "parameter":"tc-tab-content",   "input":"Communicate_tab_content"}, 

            #Find Update Table
            {"name":"Get Patient Info",   "test_element":"step",          "variable":"monitor_tables",         "command":"tagName",         "parameter":"table",   "input":"OrderSupplies_tab_content"},

            ###### There are three tables, 0-Bandages, 1-Cleanser, 2-Tissue
            {"name":"Get Select Supply row: Temp",   "test_element":"step",      "variable":"monitor_table",   "command":"getListItem",     "parameter":0,   "input":"monitor_tables"},
            {"name":"Get Supply Info rows",   "test_element":"step",          "variable":"monitor_rows",    "command":"tagName",         "parameter":"tr",   "input":"monitor_table"},
            {"name":"Get Select Supply row: Temp",   "test_element":"step",      "variable":"monitor_row",   "command":"getListItem",     "parameter":0,   "input":"monitor_rows"},
            {"name":"Get Supply Info cells",   "test_element":"step",          "variable":"monitor_cells",         "command":"tagName",         "parameter":"td",   "input":"monitor_row"},
            {"name":"Get Select Supply row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell",        "command":"getListItem",  "parameter":0,   "input":"monitor_cells"},
            {"name":"Get text fields field",   "test_element":"step",      "variable":"order_checklist",              "command":"tagName",         "parameter":"input",   "input":"monitor_cell"},
            {"name":"Get clicklist tab",   "test_element":"step",      "variable":"order_checklist-on",         "command":"click",         "parameter":0,            "input":"order_checklist"},
            {"name":"Get Select Supply row: Temp cell value",   "test_element":"step",      "variable":"monitor_cell2",        "command":"getListItem",  "parameter":1,   "input":"monitor_cells"},
            {"name":"Verify Functions",         "test_element":"verify",   "variable":"verifyFunctionResults",     "command":"compare",      "parameter":"Need to Order",    "input":"monitor_cell2"}, 

            #################################################################
            #Step 4: TODO: Tests the checklists for 1-Cleaser and 2-Tissue
            # Copy the previous block of code, and change "Get Select Supply row" parameter from 0 to 1 or 2. 
            #################################################################


            {"name":"End of Tests",         "test_element":""}]

        order_supplies = TestDriver()
        order_supplies.run_commands(driver, Order_Supplies)

        assert "No results found." not in driver.page_source
        sleep(30)
    def tearDown(self):
        print("TearDown Elements")
        self.driver.close()

if __name__ == "__main__":

    unittest.main()