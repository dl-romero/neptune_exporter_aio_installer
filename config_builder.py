import os
import socket
import yaml

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

class ConfigBuilder:
    def __init__(self):
        self.default_neptune_apex = str(os.path.dirname(__file__)) + "/apps/neptune_exporter/configuration/apex.yml"
        self.default_neptune_fusion = str(os.path.dirname(__file__)) +"/apps/neptune_exporter/configuration/fusion.yml"
        self.default_prometheus = str(os.path.dirname(__file__)) + "/apps/prometheus/prometheus.yml"

    def main_menu(self):
        print("-----------------------------------------------------------")
        print("This tool will build your configuration files for the Neptune Apex, Neptune Fusion, and Prometheus.")
        print("It is meant for fresh installations only. Use at your own risk.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Build Apex configuration file.")
        print("2. Build Fusion configuration file.")
        print("3. Build Prometheus configuration file.")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2, 3]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                self.build_apex_menu()
            elif menu_selection == 2:
                self.build_fusion_menu()
            elif menu_selection == 3:
                self.build_prometheus_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

    def build_apex_menu(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure the apex.yml file.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Configure file for fresh installation.")
        print("2. Return to Main Menu.")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                self.build_apex_1()
            elif menu_selection == 2:
                self.build_prometheus_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

    def build_apex_1(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure apex.yml file for fresh installation")
        print("-----------------------------------------------------------")
        print("Note: If all of your Neptune Apex devices use the default login there is no need to continue.")
        print("")
        print("1. Continue.")
        print("2. Go Back. ")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                print("")
                total_apex_to_configure = int(input("How many of Neptune Apex credendials do you have? "))
                while total_apex_to_configure <= 0:
                    print("Please enter a number greater than zero.")
                    total_apex_to_configure = int(input("How many of Neptune Apex credendials do you have? "))
                    
                for apexes_to_configure in range(total_apex_to_configure):
                    with open(self.default_neptune_apex) as f:
                        apex_cfg = yaml.load(f, Loader=yaml.FullLoader)

                    apex_auths = apex_cfg["apex_auths"]
                    current_auth_list = list(apex_auths.keys())
                    print("")
                    print("Current Auth Names Stored: {}".format(current_auth_list))

                    print("")
                    print("Note: The name you give the Apex Authenticaiton will be converted to all lowercase and spaces replaced with underscores.")
                    apex_auth_name_to_configure = input("What would you like to name Apex Authentication #{}? ".format(apexes_to_configure + 1))
                    while str(apex_auth_name_to_configure).replace(" ", "") in ["", "None", None]:
                        apex_auth_name_to_configure = input("This Apex Auth Name cannot be blank/empty. Please try again.\nWhat would you like to name this Apex Authentication #{}? ".format(apexes_to_configure + 1))
                    while apex_auth_name_to_configure in current_auth_list:
                        apex_auth_name_to_configure = input("This Apex Auth Name is already in use. Please try another name.\nWhat would you like to name this Apex Authentication #{}? ".format(apexes_to_configure + 1))
                    
                    # Getting the auth username
                    apex_auth_username_to_configure = input("What is the username for the Apex Authentication '{}'? ".format(apex_auth_name_to_configure))
                    while str(apex_auth_username_to_configure).replace(" ", "") in ["", "None", None]:
                        apex_auth_username_to_configure = input("The username cannot be blank/empty. Please try again.\nWhat is the username for this Apex Authentication '{}'? ".format(apex_auth_name_to_configure))

                    # Getting the auth password
                    apex_auth_password_to_configure = input("What is the password for this Apex Authentication '{}'? ".format(apex_auth_name_to_configure))
                    while str(apex_auth_password_to_configure).replace(" ", "") in ["", "None", None]:
                        apex_auth_password_to_configure = input("The password cannot be blank/empty. Please try again.\nWhat is the username for this Apex Authentication '{}'? ".format(apex_auth_name_to_configure))
                    
                    apex_auths[str(apex_auth_name_to_configure).lower()] = {"username" : apex_auth_username_to_configure,
                                                               "password" : apex_auth_password_to_configure}
                    with open(self.default_neptune_apex, "w") as f:
                        apex_cfg = yaml.dump(apex_cfg, stream=f, default_flow_style=False, sort_keys=False)

                    print("")
                    print("Your apex.yml file has been updated with Auth Name:{}, Username: {}, Password:{}.".format(apex_auth_name_to_configure, 
                                                                                                                     apex_auth_username_to_configure, 
                                                                                                                     apex_auth_password_to_configure))  
                with open(self.default_neptune_apex) as f:
                        apex_cfg = yaml.load(f, Loader=yaml.FullLoader)      
                apex_auths = apex_cfg["apex_auths"] 
                f.close()
                print("")
                print("Your apex.yml file updates are complete and your Apex Authenicaiton modules are {}".format(list(apex_auths.keys())))
                print("")
                input("Press any key to return to the menu.")
                self.build_apex_1()

                    
            elif menu_selection == 2:
                # Go Back
                self.build_apex_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

    def build_fusion_menu(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure the fusion.yml file.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Configure file for fresh installation.")
        print("2. Return to Main Menu.")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                self.build_fusion_1()
            elif menu_selection == 2:
                self.main_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

    def build_fusion_1(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure fusion.yml file for fresh installation")
        print("-----------------------------------------------------------")
        print("")
        print("1. Continue.")
        print("2. Go Back. ")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                print("")
                total_apex_fusion_ids_to_configure = int(input("How many of Fusion Apex IDs do you have? "))
                while total_apex_fusion_ids_to_configure <= 0:
                    print("Please enter a number greater than zero.")
                    total_apex_fusion_ids_to_configure = int(input("How many of Fusion Apex IDs do you have? "))
                    
                for apex_fusion_id_to_configure in range(total_apex_fusion_ids_to_configure):
                    with open(self.default_neptune_fusion) as f:
                        fusion_cfg = yaml.load(f, Loader=yaml.FullLoader)

                    fusion_ids = fusion_cfg["fusion"]["apex_systems"]
                    current_fusion_id_list = list(fusion_ids.keys())
                    print("")
                    print("Current Fusion Apex IDs Stored: {}".format(current_fusion_id_list))
                    print("")
                    fusion_id_to_configure = input("Enter Fusion Apex ID #{}? ".format(apex_fusion_id_to_configure + 1))
                    while str(fusion_id_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_to_configure = input("The Fusion Apex ID cannot be blank/empty. Please try again.\nEnter Fusion Apex ID #{}? ".format(apex_fusion_id_to_configure + 1))
                    while fusion_id_to_configure in current_fusion_id_list:
                        fusion_id_to_configure = input("The Fusion Apex ID is already in use. Please try another name.\Enter Fusion Apex ID #{}? ".format(apex_fusion_id_to_configure + 1))
                    
                    # Getting the auth username
                    fusion_id_username_to_configure = input("What is the username for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    while str(fusion_id_username_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_username_to_configure = input("The username cannot be blank/empty. Please try again.\nWhat is the username for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))

                    # Getting the auth password
                    fusion_id_password_to_configure = input("What is the password for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    while str(fusion_id_password_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_password_to_configure = input("The password cannot be blank/empty. Please try again.\nWhat is the username for theFusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    

                    fusion_ids[fusion_id_to_configure] = {"username" : fusion_id_username_to_configure,
                                                               "password" : fusion_id_password_to_configure}
                    with open(self.default_neptune_fusion, "w") as f:
                        fusion_cfg = yaml.dump(fusion_cfg, stream=f, default_flow_style=False, sort_keys=False)

                    print("")
                    print("Your fusion.yml file has been updated with Apex ID:{}, Username: {}, Password:{}.".format(fusion_id_to_configure, 
                                                                                                                     fusion_id_username_to_configure, 
                                                                                                                     fusion_id_password_to_configure))  
                with open(self.default_neptune_fusion) as f:
                    fusion_cfg = yaml.load(f, Loader=yaml.FullLoader)      
                fusion_ids = fusion_cfg["fusion"]["apex_systems"]
                current_fusion_id_list = list(fusion_ids.keys())
                f.close()
                print("")
                print("Your fusion.yml file updates are complete and your Fusion Apex IDs are {}".format(current_fusion_id_list))
                print("")
                input("Press any key to return to the menu.")
                self.build_fusion_1()
                    
            elif menu_selection == 2:
                # Go Back
                self.build_fusion_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

    def build_prometheus_menu(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure the prometheus.yml file.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Configure file for fresh installation.")
        print("2. Return to Main Menu.")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                self.build_prometheus_1()
            elif menu_selection == 2:
                self.main_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None
    def build_prometheus_1(self):
        clear_screen()
        print("-----------------------------------------------------------")
        print("Configure prometheus.yml file for fresh installation")
        print("")
        print("Agenda:")
        print(" - Add Apex devices.")
        print(" - Add Fusion Apex IDs.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Continue.")
        print("2. Go Back. ")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                print("")
                with open(self.default_prometheus) as f:
                    prometheus_cfg = yaml.load(f, Loader=yaml.FullLoader)
                neptun_apex_jobs = {
                    'job_name': 'neptune_apex', 
                    'static_configs': [{'targets': []}],
                    'metrics_path': '/metrics/apex', 
                    'params': {'auth_module': ['default']},
                    'relabel_configs': [
                        {'source_labels': ['__address__'],
                         'target_label': '__param_target'},
                        {'source_labels': ['__param_target'],
                         'target_label': 'instance'},
                        {'target_label': '__address__',
                         'replacement': '{}:5006'.format(socket.gethostname())}]}
                
                neptinue_fusion_jobs = {
                    'job_name': 'neptune_fusion',
                    'static_configs': [{'targets': []}], 
                    'metrics_path': '/metrics/fusion', 
                    'params': {'data_max_age': [300]}, 
                    'relabel_configs': [
                        {'source_labels': ['__param_target'], 
                            'target_label': 'instance'}, 
                        {'source_labels': ['__address__'], 
                            'target_label': '__param_fusion_apex_id'}, 
                        {'target_label': '__address__', 
                            'replacement': '{}:5006'.format(socket.gethostname())}]}

                
                print("")
                ##### 
                print("")
                print("Your prometheus.yml file updates are complete")
                print("")
                input("Press any key to return to the menu.")
                self.build_fusion_1()
                    
            elif menu_selection == 2:
                # Go Back
                self.build_fusion_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

if __name__ == "__main__":
    ConfigBuilder().main_menu()