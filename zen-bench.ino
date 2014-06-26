int benchSensorValue = 0;
bool detected = false;

void setup() {
    Spark.variable("benchSensorValue", &benchSensorValue, INT);
    pinMode(A0, INPUT_PULLUP);
}

void loop() {
    benchSensorValue = analogRead(A0);
    if (detected) {
        // If we are currently in the detected mode, wait for the sensor to reach above the threshold value
        // If we are above the threshold value, set detected = false and send a finish event
        if (benchSensorValue > 25) {
            detected = false;
        }
            Spark.publish("end-detect");
        }
    } else {
        // If we are not currently in a detected mode, wait for the sensor to reach below the cut-off threshold value
        // if we are below the cut-off threshold value, set detected = true and send a start event
        if (benchSensorValue < 10) {
            detected = true;
            Spark.publish("start-detect");
        }
    }
    
    delay(1000);  // Only need to be accurate to the second.
}
