from pubsub import pub







# Call the main dashboard for the main dashbord : 
from View import dashboard
from View import add_task




# Here all the listening Functions to be done for the sending functions :
def completed_task(message_string):
    print(message_string)





pub.subscribe(listener=completed_task , topicName="timer_data")






# Here all the functions to be defined for sending the messages :