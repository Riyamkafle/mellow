import random
import time

class DefenseSystem:
    def __init__(self):
        self.intercepted_threats = 0
        self.missed_threats = 0
        self.security_level = "High"  # Initial security level is set to High

    def detect_threat(self):
        # Simulate detecting a threat
        threat_detected = random.choice([True, False])
        angle = None
        if threat_detected:
            angle = random.uniform(0, 360)  # Generate a random angle between 0 and 360 degrees
        return threat_detected, angle

    def intercept_threat(self, angle):
        # Simulate intercepting a threat
        success = random.choice([True, False])
        if success:
            self.intercepted_threats += 1
            print(f"\n Threat intercepted successfully at angle {angle:.2f} degrees!")
        else:
            self.missed_threats += 1
            print(f"\n Missed the threat at angle {angle:.2f} degrees!")
            self.update_security_level()  # Update security level when a threat is missed

    def update_security_level(self):
        # Reduce security level to Low if a threat is missed
        self.security_level = "Low"
        print("\n Security level reduced to Low due to missed threat!")

    def status_report(self):
        print(f"\n Intercepted Threats: {self.intercepted_threats}")
        print(f"\n Missed Threats: {self.missed_threats}")
        print(f"\n Current Security Level: {self.security_level}")

# Simulate the defense system in action
defense_system = DefenseSystem()

for _ in range(10):  # Simulate 10 potential threats
    threat_detected, angle = defense_system.detect_threat()
    if threat_detected:
        print(f"\n Threat detected at angle {angle:.2f} degrees!") 
        defense_system.intercept_threat(angle)
    else:
        
        print("\n No threat detected.")
    time.sleep(1)  # Pause to simulate time passing

defense_system.status_report()
