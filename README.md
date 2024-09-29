Run this python script as a service on Debian.
 
 MQTT commands are received and controls the screen blanking feature of DPMS service

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
