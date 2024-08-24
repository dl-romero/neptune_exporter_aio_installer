import os
import subprocess
import socket
import yaml
import platform
import logging.config

def setup_logger(name, log_file, level=logging.INFO):
    # Setup logging machanism
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

application_logger = setup_logger('config_builder', str(os.path.dirname(__file__)) + '/' + 'config_builder.log')
application_logger.info("--- CONFIG_BUILDER STARTED ---")
application_logger.info("OS Info: {}".format(platform.platform()))
application_logger.info("Python Version: {}".format(platform.python_version()))

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

class ConfigBuilder:
    def __init__(self):
        self.default_neptune_apex = str(os.path.dirname(__file__)) + "/apps/neptune_exporter/configuration/apex.yml"
        self.default_neptune_fusion = str(os.path.dirname(__file__)) +"/apps/neptune_exporter/configuration/fusion.yml"
        self.default_prometheus = str(os.path.dirname(__file__)) + "/apps/prometheus/prometheus.yml"
        self.prom_tools = str(os.path.dirname(__file__)) + "/apps/prometheus/"

    def main_menu(self):
        application_logger.info("Entered Main Menu")
        clear_screen()
        print("-----------------------------------------------------------")
        print("This tool will help:")
        print(" - Build your configuration files and service files for the Neptune Exporter and Prometheus.")
        print("")
        print("It is meant for fresh installations only and for those who not necessarily tech savy.")
        print("That said. Use at your own risk.")
        print("-----------------------------------------------------------")
        print("")
        print("1. Build Apex configuration file.")
        print("2. Build Fusion configuration file.")
        print("3. Build Prometheus configuration file.")
        print("4. Exit.")
        print("")
        menu_selection = None
        while menu_selection not in [1, 2, 3, 4]:
            menu_selection = int(input("Option Number: "))
            if menu_selection == 1:
                self.build_apex_menu()
            elif menu_selection == 2:
                self.build_fusion_menu()
            elif menu_selection == 3:
                self.build_prometheus_menu()
            elif menu_selection == 4:
                print("Goodbye!")
                exit()
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
                self.main_menu()
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
                print("Your apex.yml file updates are complete and your Apex Authenticaiton Modules are {}".format(list(apex_auths.keys())))
                print("")
                input("Press Enter to return to the menu.")
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
                
                apex_fusion_dict = {"fusion" : {"apex_systems" : {}}}
                for apex_fusion_id_to_configure in range(total_apex_fusion_ids_to_configure):
                    fusion_ids = apex_fusion_dict["fusion"]["apex_systems"]
                    current_fusion_id_list = list(fusion_ids.keys())
                    print("")
                    print("Current Fusion Apex IDs Stored: {}".format(current_fusion_id_list))
                    print("")
                    fusion_id_to_configure = input("Enter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    while str(fusion_id_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_to_configure = input("The Fusion Apex ID cannot be blank/empty. Please try again.\nEnter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    while fusion_id_to_configure in current_fusion_id_list:
                        fusion_id_to_configure = input("The Fusion Apex ID is already in use. Please try another name.\Enter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    
                    # Getting the auth username
                    fusion_id_username_to_configure = input("What is the username for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    while str(fusion_id_username_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_username_to_configure = input("The username cannot be blank/empty. Please try again.\nWhat is the username for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))

                    # Getting the auth password
                    fusion_id_password_to_configure = input("What is the password for the Fusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    while str(fusion_id_password_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_password_to_configure = input("The password cannot be blank/empty. Please try again.\nWhat is the username for theFusion Apex ID '{}'? ".format(fusion_id_to_configure))
                    

                    apex_fusion_dict["fusion"]["apex_systems"][fusion_id_to_configure] = {"username" : fusion_id_username_to_configure,
                                                               "password" : fusion_id_password_to_configure}
                    with open(self.default_neptune_fusion, "w") as f:
                        fusion_cfg = yaml.dump(apex_fusion_dict, stream=f, default_flow_style=False, sort_keys=False)

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
                input("Press Enter to return to the menu.")
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
        print("Configure Prometheus Service File and the prometheus.yml file for fresh installation")
        print("")
        print("Agenda:")
        print(" - Configure Prometheus Service Port")
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
                clear_screen()
                print("-----------------------------------------------------------")
                print("Configuring Prometheus Service File.")
                print("-----------------------------------------------------------")
                print("")
                print("Note: Some Linux distros come with Cockpit installed that uses port 9090.")
                print("This can cause a problem with Prometheus because its default is also 9090.")
                print("Unsure? No problem lets check real quick. Try going to https://{}:9090.".format(socket.gethostname()))
                print("If a website loads up or you plan to install Cockpit choose another port for example: 5050. Just note down what you choose")
                print("Youll need this info later when connecting Grafana and Prometheus.")
                print("")
                prometheus_port = int(input("What port number should Prometheus use (default is 9090, enter 9090 to keep it default)? "))
                while prometheus_port <= 0:
                    print("Please enter a number greater than zero.")
                    prometheus_port = int(input("What port number should Prometheus use (default is 9090, enter 9090 to keep it default)? "))
                
                with open("apps/prometheus/prometheus.service", 'r') as service_file:
                    service_file_content = service_file.read()
                    service_file_content = service_file_content.replace("<PORT>", str(prometheus_port))
                with open("apps/prometheus/prometheus.service", 'w') as service_file:
                    service_file.write(service_file_content)

                clear_screen()
                print("-----------------------------------------------------------")
                print("Configuring Apex Devices.")
                print("Have your Neptune Apex Auth Modules and associated IP Addresses ready.")
                print("-----------------------------------------------------------")
                total_apex_auths = int(input("How many of Neptune Apex Authenticaiton Modules do you have? "))
                while total_apex_auths <= 0:
                    print("Please enter a number greater than zero.")
                    total_apex_auths = int(input("How many of Neptune Apex Authenticaiton Modules do you have? "))
                for apex_auth_to_configure in range(total_apex_auths):
                    name_of_apex_auth = input("Enter the name of Neptune Apex Authenticaiton Module #{}: ".format(apex_auth_to_configure + 1))
                    ip_address_list = []
                    total_ips_for_auth = int(input("How many of IP Addresses use '{}'? ".format(name_of_apex_auth)))
                    while total_ips_for_auth <= 0:
                        print("Please enter a number greater than zero.")
                        total_ips_for_auth = int(input("How many of IP Addresses use '{}'? ".format(name_of_apex_auth)))
                    for ip_address_number in range(total_ips_for_auth):
                        ip_address_to_add = input("Enter IP Address #{}: ".format(ip_address_number + 1))
                        while str(ip_address_to_add).replace(" ", "") in ["", "None", None]:
                            ip_address_to_add = input("The IP Address cannot be blank/empty. Please try again.\nEnter IP Address #{}: ".format(ip_address_number + 1))
                        ip_address_list.append(ip_address_to_add)
                    with open(self.default_prometheus) as f:
                        prometheus_cfg = yaml.load(f, Loader=yaml.FullLoader)

                    if total_apex_auths == 1:
                        apex_auth_to_configure = ""
                    else:
                        apex_auth_to_configure = "_{}".format(apex_auth_to_configure + 1)
                    neptun_apex_job = {
                    'job_name': 'neptune_apex{}'.format(apex_auth_to_configure), 
                    'static_configs': [{'targets': ip_address_list}],
                    'metrics_path': '/metrics/apex', 
                    'params': {'auth_module': [name_of_apex_auth]},
                    'relabel_configs': [
                        {'source_labels': ['__address__'],
                         'target_label': '__param_target'},
                        {'source_labels': ['__param_target'],
                         'target_label': 'instance'},
                        {'target_label': '__address__',
                         'replacement': '{}:5006'.format(socket.gethostname())}]}
                    prometheus_cfg["scrape_configs"].append(neptun_apex_job)
                    with open(self.default_prometheus, "w") as f:
                        prometheus_cfg = yaml.dump(prometheus_cfg, stream=f, default_flow_style=False, sort_keys=False)
                clear_screen()
                print("-----------------------------------------------------------")
                print("Configuring Fusion Apex IDs.")
                print("Have your IDs ready.")
                print("-----------------------------------------------------------")
                print("")
                with open(self.default_prometheus) as f:
                    prometheus_cfg = yaml.load(f, Loader=yaml.FullLoader)
                total_apex_fusion_ids_to_configure = int(input("How many of Fusion Apex IDs do you have? "))
                while total_apex_fusion_ids_to_configure <= 0:
                    print("Please enter a number greater than zero.")
                    total_apex_fusion_ids_to_configure = int(input("How many of Fusion Apex IDs do you have? "))
                neptune_fusion_ids = []
                for apex_fusion_id_to_configure in range(total_apex_fusion_ids_to_configure):
                    with open(self.default_prometheus) as f:
                        prometheus_cfg = yaml.load(f, Loader=yaml.FullLoader)
                    print("")
                    print("Current Fusion Apex IDs Stored: {}".format(neptune_fusion_ids))
                    print("")
                    fusion_id_to_configure = input("Enter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    while str(fusion_id_to_configure).replace(" ", "") in ["", "None", None]:
                        fusion_id_to_configure = input("The Fusion Apex ID cannot be blank/empty. Please try again.\nEnter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    while fusion_id_to_configure in neptune_fusion_ids:
                        fusion_id_to_configure = input("The Fusion Apex ID is already in use. Please try another name.\Enter Fusion Apex ID #{}: ".format(apex_fusion_id_to_configure + 1))
                    neptune_fusion_ids.append(fusion_id_to_configure)
                    print("")
                    print("Fusion Apex ID: '{}' has been added to your prometheus.yml".format(fusion_id_to_configure))
                neptinue_fusion_job = {
                    'job_name': 'neptune_fusion',
                    'static_configs': [{'targets': neptune_fusion_ids}], 
                    'metrics_path': '/metrics/fusion', 
                    'params': {'data_max_age': [300]}, 
                    'relabel_configs': [
                        {'source_labels': ['__param_target'], 
                            'target_label': 'instance'}, 
                        {'source_labels': ['__address__'], 
                            'target_label': '__param_fusion_apex_id'}, 
                        {'target_label': '__address__', 
                            'replacement': '{}:5006'.format(socket.gethostname())}]}
                prometheus_cfg["scrape_configs"].append(neptinue_fusion_job)
                with open(self.default_prometheus, "w") as f:
                    prometheus_cfg = yaml.dump(prometheus_cfg, stream=f, default_flow_style=False, sort_keys=False)
                f.close()
                print("")
                print("Your prometheus.yml file updates are complete")
                print("Validating with Promtool")
                print("......")
                subprocess.run(["unzip", self.prom_tools + "promtool.zip"], shell=True)
                promtool_validation = subprocess.run(["cd", self.prom_tools, "./promtool", "check","config", self.default_prometheus], shell=True)
                if promtool_validation.returncode == 0:
                    print("......Promtool validation: Successful")
                else:
                    print("......Promtool validation: Failed.")
                    print("You will need to update the prometheus.yml manually.")

                print("")
                input("Press Enter to return to the menu.")
                self.build_prometheus_1()
            elif menu_selection == 2:
                # Go Back
                self.build_prometheus_menu()
            else:
                print("Please enter a valid number.")
                menu_selection == None

if __name__ == "__main__":
    ConfigBuilder().main_menu()