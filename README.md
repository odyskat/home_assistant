# home_assistant
Personal configuration of home assistant os. Its primary aim is sensor data collecting, visualization, and notifications (mobile) when a parameter is met (e.g. high-temperature reading). It works almost in real-time (collects reading in a set time interval of 1 min by default but can be configured as low as 1 sec without sensor malfunction). Utilizes home assistant mobile app to provide access to data and more importantly push notifications.

Features a custom-made html document embedded in an iframe window in the dashboard, containing mainly a table with temperature measurements at specific times throughout the day. This is useful in cafes, restaurants, or any fridge-storing application where the state (or private stakeholder) will carry over quality controls. Usually, a printed report is required.

Sensors (shtc3 from dfrobot or adafruit) were programed through esphome, and the configuration (.yaml) files are included in "home assistant scripts/Sensors_esphome_configuration".

Hardware and connections in "fritz files/hardware and connections.md"

![Screenshot 2023-08-14 205307](https://github.com/odyskat/home_assistant/assets/114591654/661e9a82-92ee-49b1-93b8-bc200c6c550c)

![Screenshot 2023-08-14 205332](https://github.com/odyskat/home_assistant/assets/114591654/f6442e1b-4d15-4f52-b220-0d8dd6674501)

![Screenshot 2023-08-14 205338](https://github.com/odyskat/home_assistant/assets/114591654/d6a45db6-b8f8-4f34-a2a2-d294fc274b3e)

![Screenshot 2023-08-14 205350](https://github.com/odyskat/home_assistant/assets/114591654/ccdfe121-7468-46af-bd1d-939e32121df9)

![Screenshot 2023-08-14 205403](https://github.com/odyskat/home_assistant/assets/114591654/9000ae06-d3d3-47ed-bcdd-99b74c367fd5)

# Materials used
1. Doit esp32 dev kit v1 (30 pins long, 11 pins width)
2. Adafruit shtc3 temperature and humidity sensor

Connections shown below.


![homeassistant esp32 shtc3 adafruit connection_bb](https://github.com/odyskat/home_assistant/assets/114591654/4c3f6e72-18ce-4423-b162-6810623c6dde)


![homeassistant esp32 shtc3 adafruit connection_schem](https://github.com/odyskat/home_assistant/assets/114591654/881e0cc3-7a2d-43fe-b18d-275551e52bd1)
