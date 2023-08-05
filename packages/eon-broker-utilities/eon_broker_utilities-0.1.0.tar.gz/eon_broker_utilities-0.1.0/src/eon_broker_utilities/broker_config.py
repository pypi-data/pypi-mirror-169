import configparser
config_file = configparser.ConfigParser()
 
def main():
    #define sections and their key and value pairs
    config_file["RabbitConfig"]={
            "RABBIT_USER": "admin",
            "RABBIT_PASSWORD": "admin",
            "RABBIT_HOST": "10.1.0.5",
            "RABBIT_PORT": "5672",
            "EXCHANGE_NAME" : "pre_production",
            "NEW_JOBS_ROUTING_KEY" : "dispatcher.job.ready_for_",
            "SUCCESSFUL_JOB_ROUTING_KEY" : ".job.complete",
            "FAILED_JOB_ROUTING_KEY" : ".job.failed"
            }
    config_file["FMSConfig"]={
            "FMS_HOST" : "10.1.0.5",
            "FMS_PORT" : "8007"
            }

    try:
        with open("broker_config.ini","w") as confid_object:
            config_file.write(confid_object)
        print("Config file 'broker_config.ini' created")
    except:
        print("Config File Already Exists")

if __name__=="__main__":
    main()



