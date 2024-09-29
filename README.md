These scripts allow for lcd or monitor output blanking controls featured in the DPMS service of Debian OS.
 
Create a folder on the computer that you want to control, mkdir in /etc/hadpms
 git this file into that directory and then edit the file with your local homeassistant info.
 	IP address and username & password for mqtt are required

git the hadpms.service script into /etc/systemd/system, enable script as a service on Debian.
 edit the file and change to your logged in username and save it. it will just run continously in the background.
 
 MQTT commands are received and controls the screen blanking feature of DPMS service on Debian OS

	# Example configuration.yaml entry
	#mqtt:
	- binary_sensor:
		name: LCD Display
    	state_topic: "/homeassistant/sensor/dpms/lcd"
    	payload_on: "1"
    	payload_off: "0"

Template interfaces are created in Homeassistant for manual/automated control

	#Example yaml for switch template in HomeAssistant configuration.yaml
	switch:
	- platform: template
    switches:
      vaio_display:
        friendly_name: "LCD Display"
        value_template: "{{ is_state('sensor.lcd_display', 'ON') }}"
        turn_on:
          service: mqtt.publish
          data:
            topic: "/homeassistant/sensor/dpms/lcd"
            payload: "ON"
        turn_off:
          service: mqtt.publish
          data:
            topic: "/homeassistant/sensor/dpms/lcd"
            payload: "OFF"



Example use case to Blank Monitors when room light switch is shut off or turned on

  Automation YAML for Homessistant example

 	target:
   	entity_id: switch.lcd_display
   	action: switch.turn_on
    
    Same for turning off

 	target:
  	entity_id: switch.vaio_display
	action: switch.turn_on
