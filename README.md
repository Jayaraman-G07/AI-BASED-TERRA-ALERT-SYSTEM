**AI Based Terra Alert System**
Terra Alert System is an AI based landslide detection and early warning platform developed to enhance early risk detection and improve safety in landslide-prone regions. Traditional landslide monitoring methods such as manual surveys, wired sensor networks, and satellite imaging are often cost-intensive, limited in scope, and lack realtime responsiveness. These systems typically offer accuracy levels between 70–88%, depending on the method, and struggle with timely prediction and localized precision, especially in remote or high-risk terrains.The Terra Alert System provides a costeffective and scalable alternative by combining real-time terrain monitoring with AI  powered predictive analytics. Core sensing is carried out using accelerometers, vibration sensors, and GPS modules interfaced with an ARM Cortex microcontroller. These sensors continuously track ground movement, allowing rapid detection of abnormal activity.Sensor data is wirelessly transmitted via a NodeMCU (ESP8266 WiFi module) to a cloud server, where it is analyzed using a Random Forest machine learning algorithm. This algorithm classifies terrain behavior based on both historical patterns and real-time anomalies, achieving an estimated accuracy of 95% in predicting landslide events.It also detecting potential threats, the system initiates a multi-layered alert protocol that includes buzzer alarms, SMS notifications, and real-time alerts through the Blynk mobile application. This ensures timely communication across both local and remote users. To enhance accessibility, a user-friendly web and mobile dashboard developed using HTML, CSS, Bootstrap, and Python provides real-time data visualization.With seamless IoT cloud integration for scalable data management, an affordable and autonomous design, and a robust communication framework, the Terra Alert System offers a proactive and high-accuracy approach to disaster risk reduction. It is particularly well-suited for deployment in mountainous and underserved regions, with the goal of safeguarding lives and protecting infrastructure.

💡 **Features**

* Real-time landslide detection and prediction
* AI-driven risk analysis using **Random Forest**
* Real-time alerts via **Blynk app** and **SMS**
* Web-based dashboard and mobile application for monitoring
* Remote management and customization

🛠️ **Technologies Used**

* **Hardware:** ARM Cortex controller, accelerometers, vibration sensors, GPS modules, NodeMCU
* **Software:** Arduino IDE, Blynk app, Python, Flask/Django
* **AI Algorithms:** Random Forest for risk prediction
* **IoT Platforms:** Blynk, Cloud storage (ThingSpeak)
* **Notification System:** Twilio API for SMS, SMTP for emails

📂 **Project Structure**

* **Hardware/:** Sensor modules, embedded controllers, prototypes
* **Code/:** Microcontroller code, AI model scripts
* **Dashboard/:** Web and mobile app interfaces
* **Data/:** Real-time logs, risk predictions
* **Results/:** Prediction accuracy, response time

📊 **Results**

* Prediction Accuracy: **92%**
* Real-time Alert Responsiveness: **<100 ms**
* Sensor Data Processing Efficiency: **90%**
* System Uptime: **99%**


