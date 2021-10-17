# CPU-usage
You can check the processes by CPU-usage.py. You can also set the program with specific amount of CPU memories and time. Then the program will show you the processes that are using more than the amount you set and it will warn you every minutes that you set. 

./cpu_usage_py 50M 5 
You'll get warning from the system that you're using more than 50Mega bytes, every 5 minutes. (Both M and m works.) 

./cpu_usage_py 1G 60
You'll get warning from the system that you're using more than 1 Gigabyte, ,every 5 mintues. (Both G and g works.) 

You can also check the every poccess list that is using in detail in $ cat /tmp/cpu_usage_rapport.txt 


Enable Newly Added Service: Your system service has been added to your service. Let’s reload the systemctl daemon to read new file. You need to reload this deamon each time after making any changes in service file by following command. .service file. by sudo systemctl daemon-reload
Now you can enable the service to start on system boot, also start the service using the following commands: sudo systemctl enable cpu_usage.service
sudo systemctl start cpu_usage.service
For checkingh the status of the service as following command.

